import jwt
import grpc
import time
from concurrent import futures
import random
import threading

import lms_pb2
import lms_pb2_grpc
import lms_pb2
import lms_pb2_grpc

import tutoring_pb2
import tutoring_pb2_grpc


JWT_SECRET = 'mysecret'
JWT_ALGORITHM = 'HS256'


users_db = {
    'student1': {'password': 'Sanskar', 'role': 'student'},
    'student2': {'password': 'Aarnav', 'role': 'student'},
    'student3': {'password': 'Ameer', 'role':'student'},
    'instructor1': {'password': 'instructorpass', 'role': 'instructor'}
}
active_tokens = {}

course_materials=[]
material_counter = 1
queries = []         
query_counter=1;

assignments = []
submissions = []
grades = []
assignment_counter = 1





class LMSService(lms_pb2_grpc.LMSServicer):
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.commit_index = 0
        self.last_applied = 0
        self.state = 'follower'
        self.peers = peers
        self.votes_received = 0
        self.leader_id = None
        self.election_timeout = random.uniform(10, 15)  # Random timeout between 5-10 seconds
        self.heartbeat_interval = 2  # Leader sends heartbeat every 2 seconds
        self.election_timer = threading.Timer(self.election_timeout, self.start_election)
        self.election_timer.start()
        self.leader_heartbeat_thread = None
        self.lock = threading.Lock()

    def reset_election_timer(self):
        self.election_timer.cancel()
        self.election_timeout = random.uniform(10, 15)
        self.election_timer = threading.Timer(self.election_timeout, self.start_election)
        self.election_timer.start()

    def RequestVote(self, request, context):
        

        with self.lock:
            if request.term < self.current_term:
                
                return lms_pb2.RequestVoteResponse(term=self.current_term, voteGranted=False)

            if self.state=='follower':
                return lms_pb2.RequestVoteResponse(term=request.term,voteGranted = True)
            
            if (self.voted_for is None or self.voted_for == request.candidateId) and request.term >= self.current_term:
                self.voted_for = request.candidateId
                self.current_term = request.term
                self.reset_election_timer()  # Reset the timer on valid vote request
                return lms_pb2.RequestVoteResponse(term=request.term, voteGranted=True)

            
            return lms_pb2.RequestVoteResponse(term=self.current_term, voteGranted=False)

    def AppendEntries(self, request, context):
        with self.lock:
            if request.term < self.current_term:
                print("hello world")
                print(request.term)
                print(self.current_term)
                return lms_pb2.AppendEntriesResponse(term=self.current_term, success=False)


            self.reset_election_timer()

        # Step 3: Update the current term and leader if the term is greater
            if request.term > self.current_term:
                self.current_term = request.term
                self.state = 'follower'
                self.leader_id = request.leaderId
                # Valid heartbeat or append entry
             # Check if the follower has the correct log entry at prevLogIndex
            if request.prevLogIndex >= 0 and (len(self.log) <= request.prevLogIndex or self.log[request.prevLogIndex].term != request.prevLogTerm):
            # Log doesn't contain the previous log entry, reject the append
                
                print("failed from here ")
                return lms_pb2.AppendEntriesResponse(term=self.current_term, success=False)

        # Append new entries if provided (normally this would include conflict resolution logic)
            if request.entries:
                self.log = self.log[:request.prevLogIndex + 1]  # Delete any conflicting entries
                self.log.extend(request.entries)  # Append the new log entries
                print(f"Entries succssfully appended at node - {self.node_id}")
                
        # Update the commit index
            if request.leaderCommit > self.commit_index:
                self.commit_index = min(request.leaderCommit, len(self.log) - 1)

        # Successful append
            return lms_pb2.AppendEntriesResponse(term=self.current_term, success=True)
    


    def AnnounceLeader(self, request, context):
        self.leader_id = request.leaderId
        print(f"Leader announced: {request.leaderId}")
        return lms_pb2.Empty()

    def start_election(self):
        with self.lock:
            if self.state == 'follower':
                print(f"Node {self.node_id} starting an election for term {self.current_term + 1}")
                self.current_term += 1
                self.votes_received = 1  # vote for self
                self.voted_for = self.node_id
                self.state = 'candidate'
                self.reset_election_timer()

                for peer in self.peers:
                    threading.Thread(target=self.send_request_vote, args=(peer,)).start()

    def send_request_vote(self, peer):
        with grpc.insecure_channel(peer) as channel:
            stub = lms_pb2_grpc.LMSStub(channel)
            request = lms_pb2.RequestVoteRequest(
                term=self.current_term,
                candidateId=self.node_id,
                lastLogIndex=len(self.log) - 1,
                lastLogTerm=self.log[-1].term if self.log else 0,
            )
            while self.state == 'candidate':
                try:
                    response = stub.RequestVote(request)
                    if response.voteGranted:
                        with self.lock:
                            self.votes_received += 1
                            print(f"Node {self.node_id}: Received vote from {peer}, total votes: {self.votes_received}")

                            # Check if we have the majority of votes
                            if self.votes_received >= len(self.peers) // 2:
                                self.become_leader()
                                return  # Stop requesting votes after becoming the leader
                    break  # Exit the loop if request succeeds
                except grpc.RpcError:
                    print(f"Node {self.node_id}: Failed to contact peer {peer}. Retrying...")
                    time.sleep(2)  # Retry after 2 seconds if peer is unreachable

    def become_leader(self):
        print(f"Node {self.node_id} becomes the leader for term {self.current_term}")
        self.state = 'leader'
        self.election_timer.cancel()  # No election timeout when the node is leader
        self.start_heartbeat_thread()

    def start_heartbeat_thread(self):

        def send_heartbeats():
            while self.state == 'leader':
                for peer in self.peers:   
                    # Send empty heartbeat if no log entries
                    threading.Thread(target=self.send_append_entries, args=(peer, None)).start()
            
                time.sleep(self.heartbeat_interval)

        self.leader_heartbeat_thread = threading.Thread(target=send_heartbeats)
        self.leader_heartbeat_thread.start()

    def GradeSubmission(self,request,context):
        with self.lock:
            if self.state != 'leader':
            # Redirect client to the current leader
                return lms_pb2.GradeSubmissionReply(success=False)

        # Create the grade_entry from the request
            grade_entry = {
                "assignment_id": request.assignment_id,
                "student_id": request.student_id,
                "grade":request.grade,
                "feedback": request.feedback
            }

        # Append the grade_entry to the log
            log_entry = lms_pb2.LogEntry(
                term=self.current_term,
                grade_entry=lms_pb2.Grade(
                    assignment_id=request.assignment_id,
                    student_id=request.student_id,
                    grade=request.grade,
                    feedback=request.feedback
                )
            )
            self.log.append(log_entry)

        # Replicate the log entry to followers
            for peer in self.peers:
                threading.Thread(target=self.send_append_entries, args=(peer, log_entry)).start()

            return lms_pb2.GradeSubmissionReply(success=True)
        
    def send_append_entries(self, peer,log_entry,heartbeat = False):
        
        with grpc.insecure_channel(peer) as channel:
            stub = lms_pb2_grpc.LMSStub(channel)

            if len(self.log) == 0:
            # No previous log entry (sending the first one)
                prevLogIndex = -1
                prevLogTerm = 0
            elif len(self.log) == 1:
            # Only one entry in the log
                prevLogIndex = 0
                prevLogTerm = self.log[0].term
            else:
            # Normal case, there are multiple log entries
                prevLogIndex = len(self.log) - 2  # Index of the previous log entry
                prevLogTerm = self.log[prevLogIndex].term

            request = lms_pb2.AppendEntriesRequest(
                term=self.current_term,
                leaderId=self.node_id,
                prevLogIndex=prevLogIndex,  # Send the correct prevLogIndex
                prevLogTerm=prevLogTerm,    # Send the correct prevLogTerm
                entries=[log_entry] if log_entry else [],  # Append new log entry or empty heartbeat
                leaderCommit=self.commit_index,
            )

            try:
                response = stub.AppendEntries(request)
                if response.success:
                    print(f"Log entry successfully replicated to peer {peer}")
                else:
                    print(f"Failed to replicate log entry to peer {peer}")
            except grpc.RpcError as e:
                print(f"Error communicating with peer {peer}: {e}")

    def CheckLeader(self, request, context):
        
        if self.state =='follower':
            return lms_pb2.LeaderResponse(is_leader=False)
        else:
            return lms_pb2.LeaderResponse(is_leader=True)


    def Login(self, request, context):
        username = request.username
        password = request.password

        # Check if the user exists and password matches
        if username in users_db and users_db[username]['password'] == password:
            # Create a JWT token
            token = jwt.encode({
                'username': username,
                'role': users_db[username]['role']

            }, JWT_SECRET, algorithm=JWT_ALGORITHM)
            
            active_tokens[username] = token

            return lms_pb2.LoginResponse(token=token, success=True, role=users_db[username]['role'])
        else:
            return lms_pb2.LoginResponse(token='', success=False)


    def Logout(self, request, context):
        token = request.token

        # Decode the token to get the username
        try:
            decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            username = decoded["username"]
        except jwt.ExpiredSignatureError:
            return lms_pb2.StatusResponse(success=False, message="Token has expired")
        except jwt.InvalidTokenError:
            return lms_pb2.StatusResponse(success=False, message="Invalid token")



        # Remove the token from the active tokens
        if username in active_tokens and active_tokens[username] == token:
            del active_tokens[username]
            return lms_pb2.StatusResponse(success=True)
        else:
            return lms_pb2.StatusResponse(success=False)


    def PostCourseMaterial(self, request, context):
        global material_counter
        material = {
            "material_id": material_counter,
            "material_title": request.material_title,
            "material_content": request.material_content
        }
        course_materials.append(material)
        material_counter += 1
        return lms_pb2.PostMaterialResponse(success=True, material_id=material["material_id"])

    # New method to get all course materials
    def GetCourseMaterials(self, request, context):
        response_materials = []
        for material in course_materials:
            response_materials.append(lms_pb2.CourseMaterial(
                material_id=material["material_id"],
                material_title=material["material_title"],
                material_content=material["material_content"]
            ))
        return lms_pb2.GetCourseMaterialsReply(materials=response_materials)



    def PostQuery(self, request, context):
        global query_counter
        if request.llm_answer == "true":
            answer = getLLMAnswer(request.query_text)
            query = {
                "user_id": request.student_id,
                "query_id":query_counter,
                "query_text":request.query_text,
                "response": answer
                }
            queries.append(query)
            query_counter+=1
        else:

            query = {
                "user_id": request.student_id,
                "query_id": query_counter,
                "query_text": request.query_text,
                "response": ""
             }
            queries.append(query)
            query_counter += 1

        return lms_pb2.PostQueryReply(success=True, query_id=query["query_id"])
    
    def GetQueries(self, request, context):
        response_queries = []
        for query in queries:
            if request.user_id == "instructor1":
                response_queries.append(lms_pb2.Query(
                    query_id=query["query_id"],
                    query_text=query["query_text"],
                    response=query["response"]
            ))
            else:
                if request.user_id == query["user_id"]:
                    response_queries.append(lms_pb2.Query(
                        query_id = query["query_id"],
                        query_text = query["query_text"],
                        response = query["response"]
                        ))
        return lms_pb2.GetQueriesReply(queries=response_queries)
    
    def RespondToQuery(self, request, context):
        for query in queries:
            if query["query_id"] == request.query_id:
                query["response"] = request.response_text
                return lms_pb2.RespondToQueryReply(success=True)
        return lms_pb2.RespondToQueryReply(success=False)
    

    # Instructor posts an assignment
    def PostAssignment(self, request, context):
        global assignment_counter
        assignment = {
            "assignment_id": assignment_counter,
            "assignment_title": request.assignment_title,
            "assignment_description": request.assignment_description
        }
        assignments.append(assignment)
        assignment_counter += 1
        return lms_pb2.PostAssignmentReply(success=True, assignment_id=assignment["assignment_id"])

    # Student retrieves all assignments
    def GetAssignments(self, request, context):
        assignment_list = []
        for assignment in assignments:
            assignment_list.append(lms_pb2.Assignment(
                assignment_id=assignment["assignment_id"],
                assignment_title=assignment["assignment_title"],
                assignment_description=assignment["assignment_description"]
            ))
        
        return lms_pb2.GetAssignmentsReply(assignments=assignment_list)
 
 # Student submits an assignment
    def SubmitAssignment(self, request, context):
        submission = {
            "assignment_id": request.assignment_id,
            "student_id": request.student_id,
            "submission_content": request.submission_content
        }
        submissions.append(submission)
        return lms_pb2.SubmitAssignmentReply(success=True)

 # Instructor retrieves all submissions for an assignment
    def GetSubmissions(self, request, context):
        assignment_submissions = []
        for submission in submissions:
             assignment_submissions.append(lms_pb2.Submission(
                    assignment_id= submission["assignment_id"],
                    student_id = submission["student_id"],
                    submission_content=submission["submission_content"]
                ))
        return lms_pb2.GetSubmissionsReply(submissions=assignment_submissions)
    
    # Instructor grades an assignment and provides optional feedback
    
    def ViewGrades(self, request, context):
        student_grades = []
        student_id = request.student_id

        for log_entry in self.log:
            if log_entry.grade_entry.student_id == student_id:
                student_grades.append(lms_pb2.Grade(
                    student_id = student_id,
                    assignment_id = log_entry.grade_entry.assignment_id,
                    grade = log_entry.grade_entry.grade,
                    feedback = log_entry.grade_entry.feedback
                ))


        return lms_pb2.ViewGradesReply(grades = student_grades)
    

def getLLMAnswer(query_text):
    
    
    with grpc.insecure_channel('localhost:50052') as channel:
            tutoring_stub = tutoring_pb2_grpc.TutoringStub(channel)
            tutoring_response = tutoring_stub.getLLMAnswerResponse(
                tutoring_pb2.LLMRequest(query=query_text)
            )


    
    return tutoring_response.answer
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    lms_pb2_grpc.add_LMSServicer_to_server(LMSService(node_id,peers), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Server running on port 50053...")

    server.wait_for_termination()

if __name__ == "__main__":
    node_id=3
    peers = ['0.0.0.0:50051','0.0.0.0:50052']
    serve()
