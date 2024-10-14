# Algorithmic Complexity Empirical Analysis

### Contributors
- Amay Viswanathan Iyer (s3970066)
- Nga Phuong (s3757362)

### Overview
This project aimed to implement a dictionary capable of supporting operations such as **Add**, **Search**, **Delete**, and **Autocomplete**. The project employed three different data structures: **Array**, **Linked List**, and **Trie**. This comprehensive implementation enabled us to assess the computational efficiencies and operational nuances of each data structure, particularly in the context of space and time complexities.

The dictionary was implemented to handle the word completion problem, providing foundational insights into the complexities of different algorithms in terms of performance and efficiency. Our work focused on evaluating each data structure for its capability to efficiently support word completion and dictionary operations with varying dataset sizes and frequencies. Specifically, we aimed to test the algorithmic space-time complexity of numerous data structures, such as arrays and linked lists, in terms of how well and quickly they are able to parse through a list of sample words.

### Achievements

#### 1. **Successful Implementation of Three Dictionary Types**
We successfully implemented the dictionary using three different data structures: **Array (Python list)**, **Linked List**, and **Trie**.
- **Array Dictionary:** Utilized Python’s built-in dynamic array to implement a word-frequency dictionary where elements were stored in alphabetical order.
- **Linked List Dictionary:** Implemented as an unsorted singly linked list where nodes stored word-frequency pairs.
- **Trie Dictionary:** Constructed a trie, a tree-like structure where nodes represented letters, facilitating faster retrieval and efficient storage of words and their frequencies.

Each implementation provided a different level of efficiency and trade-offs, allowing us to explore the distinct advantages and drawbacks of each data structure in handling various dictionary operations.


#### 2. **Performance Evaluation and Analysis**
We conducted rigorous empirical evaluations to compare the performance of the three dictionary types. The key findings were:

- **Array Dictionary**: Offers efficient random access with **O(log N)** complexity for **binary search** in a sorted array. However, **insertions** and **deletions** required reordering, making the worst-case complexity **O(N)**. This is effective for small datasets but scales poorly with increasing data sizes due to the high cost of shifting elements.
- **Linked List Dictionary**: Although **insertions** and **deletions** were efficient, given the list's flexibility in adding elements without rearranging them, **search operations** required traversing all nodes, resulting in an **O(N)** time complexity. This structure excelled in scenarios with more frequent updates compared to searches.
- **Trie Dictionary**: The **Trie** structure provided efficient handling of **search** and **insertion** operations, with a time complexity of **O(n)** where **n** is the length of the word being processed. Unlike arrays and linked lists, **Tries** leveraged prefix-based efficiency, especially for **autocomplete** operations, significantly outperforming the other structures in terms of speed and consistency.

#### 3. **Graphical Analysis and Empirical Results**
Graphical analysis provided a comprehensive visualization of the performance differences among the three data structures. 

The bar graph illustrates the runtime performances of different data structures across three distinct file sizes and corresponding word counts.

<img width="701" alt="Screenshot 2024-10-14 at 8 25 39 PM" src="https://github.com/user-attachments/assets/7349c2df-8a89-46da-bd1a-0e15d7d39231">

The line graph sheds light on runtime behavior as both file sizes and word counts increase.

<img width="1395" alt="Screenshot 2024-10-14 at 8 26 47 PM" src="https://github.com/user-attachments/assets/d840b6ef-cb2e-42a8-8d17-49da4e6120f1">

Specifically what we found was:
- **Trie dictionaries** were significantly faster in **autocomplete** tasks across all dataset sizes, demonstrating exceptional scalability. For large datasets with 200,000 words, Tries maintained efficiency while Arrays and Linked Lists showed exponential growth in runtime.
- **Array and Linked List dictionaries** had similar performance profiles for smaller datasets but diverged substantially as dataset sizes increased, with Linked Lists maintaining a smaller time overhead compared to Arrays due to avoiding extensive reordering during insertions.

### Space-Time Complexity and Efficiency

- **Space Complexity**:
  - **Array Dictionary**: The space complexity was **O(N)**, storing each word-frequency pair directly. However, resizing the dynamic array incurred additional costs that could add to inefficiency during operations involving frequent insertions or deletions.
  - **Linked List Dictionary**: Required **O(N)** space, but additional overhead existed due to pointers linking nodes, leading to increased memory usage compared to an array.
  - **Trie Dictionary**: Had the highest memory overhead due to storing nodes for every character, resulting in **O(ALPHABET_SIZE * n)**, where **ALPHABET_SIZE** represents the number of possible characters. This structure was, however, highly efficient for prefix-based retrieval operations.

- **Time Complexity**:
  - **Array Dictionary**: Insertions and deletions required **O(N)** time in the worst-case scenario due to the need for maintaining sorted order.
  - **Linked List Dictionary**: Provided **O(1)** time complexity for insertions and deletions at the beginning or end, but **O(N)** for searches, resulting in inefficiency for large-scale data operations.
  - **Trie Dictionary**: Enabled **O(n)** complexity for most operations, focusing on word length rather than the total number of words stored. This provided a consistent and efficient time complexity irrespective of the dataset size, particularly benefiting the autocomplete feature.

The project aimed to explore how these data structures handle typical operations like **Add**, **Search**, **Delete**, and **Autocomplete** in a dictionary application and to evaluate their space and time complexities for different dataset sizes.

Our findings (as detailed in the report [70†source]) indicate that the **Trie dictionary** consistently outperformed other data structures in terms of **autocomplete** operations due to its prefix-based nature. The **Array dictionary** struggled with large-scale data manipulation due to costly **insertions** and **deletions**, whereas the **Linked List** provided more flexibility but was still hampered by linear search times.

### Importance of the Project and Industrial Application
This project offers significant insight into data structures and their respective efficiencies in managing real-world problems such as **autocomplete**. Such a feature is prevalent in applications like search engines, code editors, and email clients, underscoring its importance in user experience and efficiency.

- **Scalable Autocompletion**: By leveraging the Trie data structure, our implementation mimics real-world scenarios seen in predictive text systems. The **efficiency** of the Trie structure for prefix matching aligns with industrial needs for providing quick suggestions in search engines and other content-based applications.
- **Performance-Centric Design**: The findings offer important lessons regarding choosing the right data structure for performance-centric scenarios. In industry, balancing **memory overhead** with **operation speed** is crucial for large-scale systems, making the insights from this project applicable to fields such as **database indexing**, **natural language processing**, and **data retrieval systems**.
- **Optimization for Use-Cases**: The project highlights that different data structures have distinct benefits depending on the type and frequency of operations. This serves as a reminder of the importance of selecting the correct data structure in industry, where optimizing for specific use cases can have a substantial impact on overall system performance.

### Conclusion
Our project underscores the practical importance of selecting appropriate data structures for dictionary operations. While **Array** and **Linked List** structures have their advantages, the **Trie** structure stood out in terms of both time efficiency and scalability for large datasets, particularly for autocomplete functionalities.

For industrial applications where **speed** and **accuracy** of suggestions are pivotal, such as in **search engines** or **mobile input keyboards**, **Trie dictionaries** provide a clear advantage due to their optimized prefix-based search capabilities. The project's exploration into the trade-offs between different data structures and the implications of these choices on **time-space complexity** will be valuable for future projects aimed at enhancing data retrieval and storage systems.

### File Overview

#### 1. **array_dictionary.py**
This file contains the implementation of the dictionary using an **array-based** approach, leveraging Python’s list. It provides methods for **inserting**, **searching**, **deleting**, and **autocomplete** functionalities. The array-based dictionary maintains sorted order, which helps in efficient searching but requires additional time for insertion and deletion.

#### 2. **linkedlist_dictionary.py**
This file implements the **linked list-based** dictionary. It uses a singly linked list structure to store word-frequency pairs, providing flexibility in **insertions** and **deletions**. However, **searching** operations are relatively slower due to the need to traverse the entire list.

#### 3. **trie_dictionary.py**
This file contains the implementation of the **Trie-based** dictionary, which represents words as nodes in a tree. This structure excels at **autocomplete** and **prefix matching** tasks, providing significant efficiency gains over other data structures.

#### 4. **base_dictionary.py**
This serves as an **abstract base class** for the dictionary implementations. It defines the common interface and structure that each specific dictionary type (Array, Linked List, Trie) must follow.

#### 5. **dictionary_file_based.py**
This file allows for **file-based operations** on the dictionary. It manages loading and saving dictionary data to and from files, making the system more versatile in handling persistent data.

#### 6. **dictionary_file_based_runtime_test.py**
This script is used to evaluate the **runtime performance** of the dictionary implementations. It measures the time taken for different operations across different data structures, providing empirical evidence for performance comparisons.

#### 7. **dictionary_test_script.py**
This file is a **test script** designed to validate the functionality of each dictionary implementation. It runs various test cases to ensure that all operations (add, search, delete, autocomplete) work as expected.

#### 8. **word_frequency.py**
This module is used to **analyze word frequency** in a given text file. It extracts word frequencies and provides data for populating the dictionaries, which are then used for various operations.

#### 9. **sampleData.txt, sampleData200k.txt, sampleDataToy.txt**
These files are **sample datasets** used for testing the dictionary implementations. They contain different numbers of words to evaluate the scalability and performance of the dictionaries under varying loads.

#### 10. **Test Files (test1.in, test1.out, test2.in, test2.out, testToy.in, testToy.exp, etc.)**
These files contain **input and expected output** for test cases. They are used to validate the accuracy of the dictionary operations by running automated tests and comparing the results against the expected outputs.

#### 11. **\_\_init\_\_.py**
This file makes the directory a **Python package**, allowing the dictionary modules to be imported and used together seamlessly.
