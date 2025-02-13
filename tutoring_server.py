import grpc
from concurrent import futures
import tutoring_pb2
import tutoring_pb2_grpc

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = 'deepset/roberta-base-squad2'
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

textData =  """Object-oriented programming (OOP) is a programming paradigm centered around the concept of "objects." These objects are instances of classes, which define a blueprint for the objects' behavior and attributes. OOP is built upon four main principles: encapsulation, inheritance, polymorphism, and abstraction. Encapsulation refers to the bundling of data and methods that operate on the data within a single unit, typically called a class, and restricting direct access to some of the object's components. Inheritance allows one class to inherit properties and methods from another class, promoting code reusability. Polymorphism allows objects of different classes to be treated as objects of a common superclass, even if each subclass implements methods in its own way.

Data structures are ways to organize and store data so that it can be used efficiently. Common data structures include arrays, linked lists, stacks, queues, and trees. Arrays are a collection of elements stored at contiguous memory locations. They are accessed by an index, allowing for quick retrieval but with a fixed size. Linked lists, on the other hand, consist of nodes that are connected by pointers, allowing for dynamic memory allocation but requiring sequential access to elements. Stacks are a Last In, First Out (LIFO) data structure, where the last element added is the first one to be removed. Queues follow a First In, First Out (FIFO) structure, where the first element added is the first one to be removed.

Recursion is a technique in programming where a function calls itself to solve smaller instances of a problem. It is often used in algorithms like tree traversal or sorting, such as quicksort. Quicksort is a divide-and-conquer algorithm that selects a pivot, partitions the array into two sub-arrays—one with elements smaller than the pivot and the other with elements larger than the pivot—and recursively sorts the sub-arrays. Dynamic programming is another algorithmic technique that solves complex problems by breaking them down into simpler subproblems and storing the results of subproblems to avoid redundant calculations. Memoization, a key component of dynamic programming, is used to store results and prevent recalculating the same values.

Big O notation is a mathematical notation used to describe the performance of algorithms in terms of their time and space complexity. It provides an upper bound on the time an algorithm will take relative to the size of its input. For example, an algorithm with O(n) time complexity means that the running time grows linearly with the size of the input, while O(log n) indicates that the time grows logarithmically. Efficient algorithms like binary search, which operates in O(log n) time, are highly sought after in computational problems.

A hash table is a data structure used for fast data retrieval. It maps keys to values using a hash function, which computes an index into an array where the desired data can be found. Hash tables offer average time complexity of O(1) for insertions, deletions, and lookups, making them one of the most efficient data structures for such operations. However, collisions can occur when two keys hash to the same index, and techniques like chaining or open addressing are used to handle such cases.

Graphs are another important data structure in computer science, used to represent relationships between objects. A graph consists of nodes (or vertices) and edges connecting them. Breadth-first search (BFS) and depth-first search (DFS) are two common algorithms for traversing graphs. BFS explores nodes level by level, while DFS dives deep into one branch before backtracking. Dijkstra's algorithm is a popular algorithm for finding the shortest path between nodes in a weighted graph, using a priority queue to explore the nodes with the smallest known distance from the source.
"""

class TutoringServer(tutoring_pb2_grpc.TutoringServicer):
    

    def getLLMAnswerResponse(self, request, context):
        
        QA_input = {
            'question': request.query,
            'context': textData
        }
        res = nlp(QA_input)
        ans = res['answer']
        return tutoring_pb2.LLMResponse( answer=ans)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tutoring_pb2_grpc.add_TutoringServicer_to_server(TutoringServer(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    print("Server running on port 50054...")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
