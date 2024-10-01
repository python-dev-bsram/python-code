## Objected - Oriented Goals

1. **Robustness** Ensures the software can handle errors and unexpected conditions like it has to handle the unexpected inputs rest of defined inputs.

2. **Adaptability**  Refers to how easily software can portable in different systems and accommodate changes.

3. **Reusability**  The software components can be used across different systems and applications without modification.

![Screenshot 2024-09-30 165011](https://github.com/user-attachments/assets/792353bd-1a6e-4a09-acd0-e122cd1e4aec)


## Object-Oriented Design Principles:

### Modularity

- Modularity means organizing software into separate parts or components.  Just like a house is divided into systems (electrical, plumbing), software has separate modules.  
- Each module in software handles a specific function and works together with other modules.

- In Python, a module is a file that contains related functions and classes.

#### Examples of Python modules:
- `math` module for mathematical functions
- `os` module for interacting with the operating system

#### Benefits of modularity:
- Easier to test and fix smaller components individually.
- Makes it easier to reuse modules in different projects.
- Data structures can be designed in a general way, making them reusable in many applications.

![Screenshot 2024-10-01 095756](https://github.com/user-attachments/assets/dc66b657-16ac-4270-9da2-6e7317a26d7f)

### Abstraction

- Abstraction is the layer which is binded with implementation of methods .

- ABC defines common methods but cannot be directly used to create objects.

- Abstraction simplifies the complex system to focus on core components.

- It involves naming parts of the system and explaining what they do, not how they work.

- Python also supports abstraction through abstract base classes (ABC).

- Sub classes inherit from an ABC and implement its required methods.

**Example:**

Imagine you're designing a system to represent different types of vehicles. The concept of abstraction helps you focus on the core properties and behaviors of a vehicle (e.g., starting the engine, stopping the engine) without worrying about the specific details of how each vehicle (like a car or a bike) implements these behaviors.

![Screenshot 2024-10-01 102720](https://github.com/user-attachments/assets/e8669a9b-c931-49dc-a7af-602b1298688d)



#### Enscapsulation:

- Enscapsulation is hiding the internal details of the components (class).
  
- Components should only expose a public interface for others to interact with, not the internal workings.

- The benefit of encapsulation is that one programmer can modify a component’s internals without affecting others.
Other programmers rely only on the public interface of the component, not its inner details.

- Encapsulation increases robustness and adaptability, making it easier to fix bugs or add new features with minimal changes.

- In Python, encapsulation is loosely supported through conventions.

- A class member (data or function) that starts with an underscore (e.g., _secret, __private) is considered nonpublic, private by convention.

  ![Screenshot 2024-09-30 175117](https://github.com/user-attachments/assets/215a887d-5433-4051-9782-8bfd3aada23c)

