import grpc
import lms_pb2
import lms_pb2_grpc




JWT_SECRET = 'mysecret'
token = None
role = None
user_id=None


follower_addresses = ['0.0.0.0:50051','0.0.0.0:50052','0.0.0.0:50053']  # List of follower addresses


def find_leader():
    for address in follower_addresses:
        try:
            with grpc.insecure_channel(address) as channel:
                stub = lms_pb2_grpc.LMSStub(channel)
                response = stub.CheckLeader(lms_pb2.LeaderRequest())  # Assuming CheckLeader RPC exists

                if response.is_leader:
                    print(f"Leader found at {address}")
                    return address
        except grpc.RpcError as e:
            print(f"Failed to connect to {address}")
    
    print("No leader found. Please check the cluster.")
    return None



def login(stub):
    global token, role, user_id
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_id=username
    response = stub.Login(lms_pb2.LoginRequest(username=username, password=password))

    if response.success :
        token = response.token
        role = response.role
        print(user_id)
        
        print(f"Login successful. Role: {role.capitalize()}")
    else:
        print("Login failed. Try again.")

def logout(stub):
    global token
    response = stub.Logout(lms_pb2.LogoutRequest(token=token))

    if response.success:
        print("Logout Successful")
        main_menu(stub)
    else: 
        print("Error in logging out")


def post_query(stub):
   
    query = input("Enter your query- ")
    print("1. Get answer from instructor ")
    print("2. Get answer from LLM ")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        response = stub.PostQuery(lms_pb2.PostQueryRequest(student_id = user_id,query_text = query,llm_answer = "false"))
    else:
        response = stub.PostQuery(lms_pb2.PostQueryRequest(student_id = user_id ,query_text=query,llm_answer = "true"))
    if response.success:
        print(f"Query posted successfully with ID: {response.query_id}")
        return response.query_id
    else:
        print("Failed to post query.")
        return None

def get_queries(stub):

    response = stub.GetQueries(lms_pb2.GetQueriesRequest(user_id = user_id))
    if response.queries:
        for query in response.queries:
            print(f"Query ID: {query.query_id}\nQuery: {query.query_text}\nResponse: {query.response}\n")
        
        if user_id == "instructor1":
            while True:
                print("1. Respond to query")
                print("2. Main menu")

                choice = input("Enter choice: ")

                if choice == "1":
                    respond_to_query(stub)
                else:
                    instructor_menu(stub)
    else:
        print("No queries available.")
        return []
 


def post_course_material(stub):
    material_title = input("Enter course material title: ")
    material_content = input("Enter Content: ")

    response = stub.PostCourseMaterial(lms_pb2.PostMaterialRequest(
        material_title=material_title,
        material_content=material_content
    ))
    if response.success:
        print(f"Course material posted successfully with ID: {response.material_id}\n")
        return response.material_id
    else:
        print("Failed to post course material.")
        return None

def get_course_materials(stub):
    response = stub.GetCourseMaterials(lms_pb2.GetCourseMaterialsRequest())
    if response.materials:
        for material in response.materials:
            print(f"Material ID: {material.material_id}. Title: {material.material_title}\n")
        while True:
            print("1. Read Material" )
            print("2. MainMenu ")
            choice = input("Enter your choice ")
            if choice == "1":
                material_id = int(input("Enter Material Id of content you want to read: "))
                for material in response.materials:
                    if material.material_id == material_id:
                        print(f"Material ID: {material.material_id}, Title: {material.material_title}\n")
                        print(f"Content: {material.material_content}\n")
            if choice == "2":
                student_menu(stub)
                
        return response.materials
    else:
        print("No course materials available.")
        return []


def respond_to_query(stub):
    query_id =int( input("Enter query id that you want to respond to- "))
    response_text = input("Enter response- ")

    response = stub.RespondToQuery(lms_pb2.RespondToQueryRequest(query_id=query_id, response_text=response_text))
    if response.success:
        print("Response submitted successfully.")
        return True
    else:
        print("Failed to respond to the query.")
        return False


def post_assignments(stub):

    assignment_title = input("Enter assignment title: ")
    assignment_description = input("Enter description: ")

    response = stub.PostAssignment(lms_pb2.PostAssignmentRequest(
        assignment_title=assignment_title,
        assignment_description=assignment_description
    ))
    if response.success:
        print(f"Assignment posted successfully with ID: {response.assignment_id}\n")
        return response.assignment_id
    else:
        print("Failed to post assignment.")
        return None


# Function to get all assignments (student)
def get_assignments(stub):

    response = stub.GetAssignments(lms_pb2.GetAssignmentsRequest())
    if response.assignments:
        print("Available assignments:")
        for assignment in response.assignments:
            print(f"ID: {assignment.assignment_id}. Title: {assignment.assignment_title}\n Description:  {assignment.assignment_description}\n")

        while True:
            print("\n1. Submit assignment")
            print("2. Main Menu()")

            choice = input("Enter your choice: ")
            if choice == "1":
                submit_assignment(stub)
            if choice == "2":
                student_menu(stub)
        
        return response.assignments
    else:
        print("No assignments available.")
        return []


def submit_assignment(stub):
    global user_id
    assignment_id = int(input("Enter assignment id you want to submit: "))
    submission_content = input("submit your solution: ")
    response = stub.SubmitAssignment(lms_pb2.SubmitAssignmentRequest(
        assignment_id=assignment_id,
        student_id=user_id,
        submission_content=submission_content
    ))
    if response.success:
        print(f"Assignment submitted successfully for assignment ID: {assignment_id}\n")
    else:
        print("Failed to submit assignment.")


def get_submissions(stub):

    response = stub.GetSubmissions(lms_pb2.GetSubmissionsRequest())
    if response.submissions:
        print(f"Submissions for assignments :")
        for submission in response.submissions:
            print(f"Student Name: {submission.student_id} \nAssignemt_id: {submission.assignment_id} \nSubmission: {submission.submission_content}\n")
            
        while True:

            print("1. Grade Submission")
            print("2. Main Menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                grade_submission(stub)
            else:
                instructor_menu(stub)
        return response.submissions
    else:
        print(f"No submissions found ")
        return []


def grade_submission(stub):
    global user_id
    global user_id
    try:
        student_id = input("Enter student Name you want to grade: ")
        assignment_id = int(input("Enter assignment id that you want to grade: "))
        grade = input("Enter grade: ")
        feedback = input("Enter feedback: ")

        response = stub.GradeSubmission(lms_pb2.GradeSubmissionRequest(
            assignment_id=assignment_id,
            student_id=student_id,
            grade=grade,
            feedback=feedback
        ))

        if response.success:
            print(f"Successfully graded student {student_id} for assignment ID {assignment_id} with grade {grade}.\n")
            if feedback:
                print(f"Feedback: {feedback}\n")
        else:
            print("Failed to grade the student's assignment.")
    except grpc.RpcError as e:
        print(f"Error during grading")
        print("Attempting to find a new leader...")
        leader_address = find_leader()
        if leader_address:
            with grpc.insecure_channel(leader_address) as new_channel:
                stub = lms_pb2_grpc.LMSStub(new_channel)
                grade_submission(stub)  # Retry with the new leader
        else:
            print("No leader found. Grading operation failed.")

def view_grades(stub):
    global user_id
    try:
        response = stub.ViewGrades(lms_pb2.ViewGradesRequest(student_id=user_id))
        if response.grades:
            for grade in response.grades:
                print(f"Assignment Id: {grade.assignment_id}     Grade : {grade.grade}\nFeedback: {grade.feedback}\n")
        else:
            print("No grades available.")
    except grpc.RpcError as e:
        print(f"Error during viewing grades")
        print("Attempting to find a new leader...")
        leader_address = find_leader()
        if leader_address:
            with grpc.insecure_channel(leader_address) as new_channel:
                stub = lms_pb2_grpc.LMSStub(new_channel)
                view_grades(stub)  # Retry with the new leader
        else:
            print("No leader found. View grades operation failed.")

     
def student_menu(stub):
    while True:
        print("\n--- Student Menu ---")
        print("1. Course Material")
        print("2. Get Assignments")
        print("3. Submit Assignment")
        print("4. Post a Query ")
        print("5. Get Queries")
        print("6. View grades")
        print("7. Logout")
        print("8. Exit")
        choice = input("Enter choice: ")
        
        if choice== "1":
            get_course_materials(stub)
        elif choice == "2":
            get_assignments(stub)
        elif choice == "3":
            submit_assignment(stub)
        elif choice == "4":
            post_query(stub)
        elif choice == "5":
            get_queries(stub)
        elif choice == "6":
            view_grades(stub)
        elif choice == "7":
            logout(stub)
            main_menu(stub)
        elif choice == "8":
            exit()
        else:
           print("Invalid choice. Try again.")



def instructor_menu(stub):
    while True:
        print("\n--- Instructor Menu ---")
        print("1. Post course material")
        print("2. Post Assignment")
        print("3. View Submissions")
        print("4. Check queries posted by students")
        print("5. Logout")
        print("6. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            post_course_material(stub)
        elif choice == "2":
            post_assignments(stub)
        elif choice == "3":
            get_submissions(stub)
        elif choice == "4":
            get_queries(stub)
        elif choice == "5":
            logout(stub)
        elif choice == "6":
            exit()
        else:
            print("Invalid choice. Try again.")


def main_menu(stub):
    while True:
        print("\n--- Main Menu ---")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            login(stub)
            if role == "student":
                student_menu(stub)
                print('success')
        
            elif role == "instructor":
                instructor_menu(stub)
        elif choice == "2":
            exit()
        else:
            print("Invalid choice. Try again.")

def run():
    
    leader_address = find_leader()  # Get the leader address before making RPC calls

    if leader_address:
        with grpc.insecure_channel(leader_address) as channel:
            stub = lms_pb2_grpc.LMSStub(channel)
            main_menu(stub)
    else:
        print("Unable to connect to a leader. Exiting.")


if __name__ == '__main__':

    run()
