# Java Interview Questions

A comprehensive collection of **500+ interview questions** covering all major topics for Senior Java Developer interviews. Each question includes answers structured across three levels: 🟢 Junior, 🟡 Middle, and 🔴 Senior.

---

## Structure

Every answer follows the same format:

- **🟢 Junior Level** — Simple definitions, basic concepts, easy examples
- **🟡 Middle Level** — Internal mechanics, practical usage, common mistakes, trade-offs
- **🔴 Senior Level** — Deep implementation details, architectural decisions, edge cases, performance benchmarks, production scenarios, best practices

---

## Table of Contents

### 1. Databases SQL PostgreSQL (21 questions)
1. What are indexes and why are they needed
2. How does B-tree index work
3. What is a composite index
4. When should you create an index
5. What are the disadvantages of indexes
6. What is index cardinality
7. What JOIN types exist
8. Difference between INNER JOIN and LEFT JOIN
9. What is better — JOIN or subquery
10. What is a correlated subquery
11. Difference between WHERE and HAVING
12. What does GROUP BY do
13. When to use HAVING
14. What are Window Functions
15. What does ROW_NUMBER() do
16. What does RANK() and DENSE_RANK() do
17. How does MVCC work in PostgreSQL
18. What is VACUUM in PostgreSQL
19. Why is ANALYZE needed
20. What is explain plan
21. How to optimize slow queries

### 2. Design Patterns (16 questions)
1. What are design patterns
2. What pattern categories exist
3. What is Singleton
4. How to implement a thread-safe Singleton
5. What is double-checked locking
6. What are the problems with Singleton
7. Difference between Factory Method and Abstract Factory
8. When to use Builder
9. What is Prototype pattern
10. When to use Strategy
11. How is Observer implemented in Java
12. Advantage of Decorator over inheritance
13. Difference between State and Strategy
14. What Proxy types exist
15. What is Iterator pattern
16. What anti-patterns do you know

### 3. Memory and Garbage Collection (28 questions)
1. Difference between Heap and Stack
2. What is stored in Heap
3. What is stored in Stack
4. What is Garbage Collection
5. When does an object become eligible for GC
6. What is a memory leak in Java
7. How can a memory leak occur in Java
8. What are GC generations (young, old, metaspace)
9. What is Young Generation
10. What is Old Generation (Tenured)
11. What is Metaspace (or PermGen)
12. What GC algorithms exist
13. What is G1 GC
14. What is ZGC
15. What is Shenandoah GC
16. What is stop-the-world
17. Which GCs minimize stop-the-world pauses
18. What are -Xms and -Xmx parameters
19. What happens on OutOfMemoryError
20. What OutOfMemoryError types exist
21. What is a memory leak and how to detect it
22. What tools help analyze memory
23. What is a heap dump
24. How to get a heap dump
25. What are GC roots
26. What is reachability in GC context
27. Can you manually trigger GC
28. Why you should not call System.gc()

### 4. Collections (31 questions)
1. What are the main Collection Framework interfaces
2. Difference between List, Set and Queue
3. Difference between ArrayList and LinkedList
4. When to use ArrayList vs LinkedList
5. Time complexity of operations in ArrayList
6. Time complexity of operations in LinkedList
7. What is Vector and how does it differ from ArrayList
8. What is Stack
9. What is Queue and what implementations exist
10. What is Deque
11. Difference between HashSet, LinkedHashSet and TreeSet
12. How does HashSet work internally
13. What is TreeSet and how does it work
14. What is Map and what implementations exist
15. Difference between HashMap, LinkedHashMap and TreeMap
16. When to use TreeMap
17. What is WeakHashMap
18. What is ConcurrentHashMap
19. How does ConcurrentHashMap ensure thread-safety
20. What is CopyOnWriteArrayList
21. When to use synchronized collections
22. How to get a synchronized collection
23. What is Collections.unmodifiableList()
24. How does Collections.unmodifiableList() work internally
25. Difference between Iterator and ListIterator
26. What are fail-fast and fail-safe iterators
27. What is ConcurrentModificationException
28. How to properly remove elements during iteration
29. What are Comparable and Comparator
30. Difference between Comparable and Comparator
31. What operations does the Collection interface support

### 5. Spring Spring Boot (29 questions)
1. What is Dependency Injection
2. Difference between constructor, setter and field injection
3. Which injection type is recommended and why
4. What is a Bean in Spring
5. How to create a Bean in Spring
6. What is Bean Lifecycle
7. What are the Bean lifecycle stages
8. What is BeanPostProcessor
9. What do @PostConstruct and @PreDestroy methods do
10. What is Bean scope
11. What scopes exist in Spring
12. Difference between singleton and prototype scope
13. What is a proxy in Spring
14. When does Spring create a proxy
15. What is AOP (Aspect-Oriented Programming)
16. What are aspect, advice, pointcut, join point
17. What does @Transactional do
18. Why @Transactional does not work with self-invocation
19. How to solve the self-invocation problem
20. What is auto-configuration in Spring Boot
21. How does @SpringBootApplication work
22. What is a starter in Spring Boot
23. What does @ComponentScan do
24. What is a @Configuration class
25. Difference between @Component, @Service, @Repository, @Controller
26. What does @Autowired do
27. What to do if there are multiple beans of the same type
28. What is @Qualifier
29. What are profiles in Spring

### 6. REST HTTP (30 questions)
1. What is REST
2. What does Stateless mean in REST context
3. What are the main HTTP methods used in REST
4. Difference between PUT and PATCH
5. What is idempotency
6. Which HTTP methods are idempotent
7. Why GET and DELETE are idempotent
8. Is POST idempotent
9. What HTTP status codes do you know
10. Difference between 401 and 403
11. What is RESTful API design
12. How to properly name REST endpoints
13. Should you use verbs in URL
14. What is HATEOAS
15. How to organize REST API versioning
16. What is Content-Type header
17. What is Accept header

### 7. Exceptions (28 questions)
1. Difference between checked and unchecked exceptions
2. What is a checked exception and when to use it
3. What is an unchecked exception (Runtime Exception)
4. Which exceptions must be handled
5. What is at the top of the exception hierarchy
6. What is Throwable
7. Difference between Error and Exception
8. Is the finally block guaranteed to execute
9. What is try-with-resources
10. What are the requirements for resources in try-with-resources
11. What is the AutoCloseable interface
12. Difference between AutoCloseable and Closeable
13. Can you create custom exceptions
14. When should you create your own exceptions
15. What is better — extend Exception or RuntimeException
16. What is a stack trace
17. What does printStackTrace() do
18. How to properly log exceptions
19. What is exception wrapping
20. Why you should not swallow exceptions (empty catch)
21. What does the throws keyword do
22. Can you throw a checked exception from a method without throws
23. What happens if an exception occurs in the finally block
24. What are suppressed exceptions
25. Can you have multiple catch blocks for one try
26. What is multi-catch
27. In what order should catch blocks be arranged
28. Can you re-throw an exception

### 8. Stream API (29 questions)
1. What advantages does Stream API provide
2. Difference between intermediate and terminal operations
3. What does filter() do
4. What does map() do
5. What does collect() do
6. What is a Collector and what built-in Collectors exist
7. What does flatMap() do
8. Difference between map() and flatMap()
9. What are parallel streams
10. When to use parallel streams
11. How to create a parallel stream
12. What potential problems can occur with parallel streams
13. What is ForkJoinPool and how is it related to parallel streams
14. Can you modify external variables' state in Stream operations
15. What are side effects in Stream
16. Why you should avoid side effects in Stream
17. What does reduce() do
18. Difference between reduce() and collect()
19. What is peek() and when to use it
20. Can you reuse a Stream
21. What is lazy evaluation in Stream
22. When does Stream execution begin
23. What do distinct(), sorted(), limit(), skip() do
24. How does short-circuiting work in Stream
25. What are anyMatch(), allMatch(), noneMatch()
26. What do findFirst() and findAny() do
27. How to collect a Stream into Map
28. What to do with key collisions when collecting into Map
29. How to work with Optional in Stream

### 9. Multithreading (28 questions)
1. Difference between synchronized and volatile
2. What is happens-before relationship
3. What is the visibility problem
4. What is a monitor in Java
5. How does synchronized work at the monitor level
6. Difference between synchronized method and synchronized block
7. What is reentrant lock
8. What are Atomic classes
9. What is CAS (Compare-And-Swap)
10. How do AtomicInteger and AtomicLong work
11. Advantage of Atomic classes over synchronized
12. What is a Thread Pool
13. What Thread Pool types exist in Java
14. What does ExecutorService do
15. Difference between Executors.newFixedThreadPool() and newCachedThreadPool()
16. What is ForkJoinPool
17. What is deadlock
18. What conditions are necessary for deadlock
19. How to prevent deadlock
20. What is race condition
21. How to avoid race condition
22. What are Virtual Threads in Java 21
23. Advantages of Virtual Threads over regular threads
24. When should you use Virtual Threads
25. What is structured concurrency
26. Difference between Thread and Runnable
27. What are Callable and Future
28. How to properly stop a thread

### 10. HashMap equals hashCode (29 questions)
1. How is HashMap structured internally
2. What is a bucket in HashMap
3. How does HashMap determine which bucket to put an element in
4. What is a collision in HashMap
5. How does HashMap handle collisions
6. What happens when 8 elements are reached in one bucket
7. What is the equals() and hashCode() contract
8. If two objects are equal by equals(), what about their hashCode()
9. If two objects have the same hashCode(), are they necessarily equal by equals()
10. What happens if you override equals() but not hashCode()
11. What happens if you override hashCode() but not equals()
12. Can you use a mutable object as a key in HashMap
13. What happens if you modify a key after adding it to HashMap
14. What are the requirements for a HashMap key
15. Why is String often used as a key in HashMap
16. What is load factor in HashMap
17. What is capacity in HashMap
18. When does rehashing occur
19. What happens during rehashing
20. Time complexity of get() and put() in HashMap
21. When can time complexity become O(n)
22. How does HashMap work in a multithreaded environment
23. What is ConcurrentHashMap and how does it differ from HashMap
24. Can you store null keys in HashMap
25. Can you store null values in HashMap
26. Difference between HashMap and Hashtable
27. What is WeakHashMap
28. How to properly choose initial capacity for HashMap
29. HashMap vs ConcurrentHashMap — when to use which

### 11. Transactions (22 questions)
1. Decode each letter of ACID
2. What transaction isolation levels exist
3. What is Read Uncommitted
4. What is Read Committed
5. What is Repeatable Read
6. What is Serializable
7. What is a Dirty Read
8. What is a Non-Repeatable Read
9. What is a Phantom Read
10. What is a Lost Update
11. What is the default isolation level in PostgreSQL
12. What is the default isolation level in MySQL
13. What is Propagation in Spring
14. What does Propagation.NESTED do
15. Difference between REQUIRED and REQUIRES_NEW
16. What is the @Transactional annotation
17. At what level can you use @Transactional
18. What is rollback in transactions
19. Which exceptions trigger rollback by default
20. How to configure rollback for checked exceptions
21. What is a readonly transaction
22. What happens when a @Transactional method is called from another method of the same class

### 12. String (23 questions)
1. How does the String Pool work
2. Difference between creating String via literal and via new
3. When to use intern()
4. Why is String immutable
5. When to use StringBuilder vs StringBuffer
6. Why is StringBuffer slower than StringBuilder
7. What happens during string concatenation with the + operator
8. How does Java compiler optimize string concatenation
9. Can you use == for String comparison
10. Difference between == and equals() for String
11. Where is the String Pool stored (which memory area)
12. Can the String Pool cause OutOfMemoryError
13. What does substring() do and how did it work before Java 7
14. Why was the substring() implementation changed in Java 7
15. How does split() work
16. Difference between replace() vs replaceAll()
17. What is String encoding
18. How to properly convert String to byte[] and back
19. What are compact strings in Java 9+
20. How to determine how much memory a String occupies
21. Can you modify String contents via reflection
22. What is String deduplication in G1 GC
23. Why does String implement Comparable and CharSequence

### 13. Immutability (29 questions)
1. What is an immutable object
2. What advantages do immutable objects provide
3. How to create an immutable class in Java
4. Why is the String class immutable
5. What are the consequences of String immutability
6. Why are immutable objects thread-safe
7. What is the final keyword and how does it help create immutable classes
8. Is making all fields final sufficient for immutability
9. What to do if a field references a mutable object
10. What is a defensive copy
11. When to make a defensive copy
12. How to protect a collection from modification
13. What is Collections.unmodifiableList() and how does it work
14. Difference between shallow copy and deep copy
15. Can you inherit from an immutable class
16. Why must an immutable class be final
17. What happens if you override a getter in a subclass of an immutable class
18. How does the String pool relate to immutability
19. Can you change a String value via reflection
20. What is a Record and how does it help create immutable classes
21. Why are LocalDate and LocalDateTime immutable
22. What advantages do immutable objects have for caching
23. How does immutability affect performance
24. What are persistent data structures
25. Are there any disadvantages to immutable objects
26. How to implement the Builder pattern for an immutable class
27. Can you use immutable objects as keys in HashMap
28. What happens if you modify a mutable key in HashMap
29. How to properly work with collections in immutable classes

### 14. Docker Kubernetes (24 questions)
1. What is containerization and why is it needed
2. Difference between a container and a virtual machine
3. What is a Dockerfile
4. What are the main instructions used in a Dockerfile
5. Difference between CMD and ENTRYPOINT
6. What is a multi-stage build
7. What is Docker Compose
8. What is Kubernetes and why is it needed
9. What is a Pod in Kubernetes
10. What is a Node in Kubernetes
11. What is a Service in Kubernetes
12. What Service types exist (ClusterIP, NodePort, LoadBalancer)
13. What is a ReplicaSet
14. How does scaling work in Kubernetes
15. What is a HorizontalPodAutoscaler
16. Difference between ConfigMap and Secret
17. What is a liveness probe
18. What is a readiness probe
19. Why are health checks needed
20. What is Ingress in Kubernetes
21. What is a namespace
22. How to organize a rolling update in Kubernetes
23. What is a StatefulSet and when to use it
24. How to monitor applications in Kubernetes

### 15. Kafka (30 questions)
1. What is a topic in Kafka
2. What is a partition and why is it needed
3. How is data distributed across partitions
4. What is a message key and how does it affect partitioning
5. What is a Consumer Group
6. How does consumer balancing work within a group
7. Can you have more consumers than partitions
8. What happens when you add a new consumer to a group
9. What message delivery guarantees does Kafka provide
10. Difference between at-most-once, at-least-once and exactly-once
11. How to configure exactly-once semantics
12. What is an offset in Kafka
13. How does commit offset work
14. Difference between auto commit and manual commit
15. What is rebalancing and when does it occur
16. What is replication in Kafka
17. What are leader and follower replicas
18. What is ISR (In-Sync Replicas)
19. How does Kafka ensure fault tolerance
20. What is producer acknowledgment and what modes exist (acks=0,1,all)
21. What is a batch in Kafka producer
22. How does message compression work
23. What is an idempotent producer
24. How to handle errors when reading messages
25. What is a DLQ (Dead Letter Queue)
26. How to monitor consumer lag
27. What is a retention policy
28. How are old messages deleted from a topic
29. Can you read messages from a specific partition
30. How to implement message filtering on the consumer side

### 16. Hibernate JPA (30 questions)
1. What is the N+1 problem and how to solve it
2. Difference between Lazy and Eager loading
3. When to use Lazy vs Eager loading
4. What is LazyInitializationException and how to avoid it
5. What fetch strategies exist in Hibernate
6. What does the @BatchSize annotation do
7. Describe the Entity lifecycle in Hibernate
8. What are transient, persistent, detached, removed states
9. What is the first-level cache in Hibernate
10. What is the second-level cache and when to use it
11. How to configure the second-level cache
12. What is dirty checking in Hibernate
13. How does the flush mechanism work in Hibernate
14. Difference between persist() and merge()
15. What does the refresh() method do
16. What is EntityManager and how does it differ from Session
17. How to implement optimistic locking in JPA
18. How to implement pessimistic locking in JPA
19. What is @Version and why is it needed
20. How do cascade operations work
21. What Cascade types exist
22. What is orphan removal
23. How to properly use @OneToMany and @ManyToOne
24. What are the specifics of bidirectional relationships
25. How to avoid infinite recursion during Entity serialization
26. What is JPQL and how does it differ from SQL
27. What is the Criteria API and when to use it
28. How to use JOIN FETCH to solve the N+1 problem
29. What is projection in JPA
30. What inheritance types does JPA support

### 17. Microservices (26 questions)
1. What is the Saga pattern and when to use it
2. Difference between choreography and orchestration in Saga
3. How to implement distributed transactions in microservices
4. What are compensating transactions
5. What is the Circuit Breaker pattern
6. How does Circuit Breaker work and what states does it have
7. What is Service Discovery and why is it needed
8. Difference between client-side and server-side discovery
9. What is an API Gateway and what tasks does it solve
10. What is sharding
11. Difference between sharding and partitioning
12. How to implement horizontal scaling of microservices
13. What is the Database per Service pattern
14. What problems arise from using a shared database
15. How to organize communication between microservices
16. Difference between synchronous and asynchronous communication
17. How to ensure microservice fault tolerance
18. What is the Bulkhead pattern
19. What is the Retry pattern and how to use it properly
20. What is exponential backoff
21. How to monitor a distributed microservice system
22. What is distributed tracing
23. How to implement authentication and authorization in microservices
24. What is the Strangler Fig pattern
25. How to test microservices
26. What tools are used for microservice orchestration

### 18. OOP and SOLID (22 questions)
1. What is the Single Responsibility principle and how to apply it
2. Give an example of Single Responsibility violation
3. What is the Open-Closed principle
4. How to refactor code that violates Open-Closed
5. What is the Liskov Substitution principle
6. Give an example of Liskov Substitution violation
7. What is the Interface Segregation principle
8. What is the Dependency Inversion principle
9. Why do we need SOLID principles at all
10. What are composition and inheritance
11. When is it better to use composition over inheritance
12. What is delegation in OOP
13. How is Single Responsibility related to cohesion
14. What happens if a class has multiple reasons to change
15. How does SOLID help with testing
16. How is Dependency Inversion related to Dependency Injection
17. What is the Law of Demeter (principle of least knowledge)
18. How to refactor a God Object
19. How do SOLID principles help when extending functionality
20. Can you follow all SOLID principles simultaneously
21. How to determine if a class has a single responsibility
22. What anti-patterns contradict SOLID principles

### 19. CompletableFuture and Asynchronicity (27 questions)
1. What is CompletableFuture and how does it differ from Future
2. What are the main advantages of CompletableFuture over Future
3. How to create a CompletableFuture that is already completed with a result
4. Difference between thenApply() and thenCompose()
5. What do thenAccept() and thenRun() methods do
6. How to handle exceptions in a CompletableFuture chain
7. Difference between handle(), exceptionally() and whenComplete()
8. How to combine results of multiple CompletableFutures
9. What does allOf() do and when to use it
10. What does anyOf() do and when is it useful
11. Difference between thenApply() and thenApplyAsync()
12. What thread pool is used by default for async methods
13. How to specify your own Executor for CompletableFuture
14. What is blocking code and how to distinguish it from non-blocking
15. Why it is important to avoid blocking operations in CompletableFuture
16. How to properly execute multiple parallel requests to microservices
17. What does supplyAsync() do and when to use it
18. How to cancel CompletableFuture execution
19. What happens if an exception occurs in a CompletableFuture chain
20. Can you reuse a single CompletableFuture in multiple chains
21. How to implement a timeout for CompletableFuture
22. What does orTimeout() do in Java 9+
23. Difference between thenCombine() and thenCompose()
24. How to test code with CompletableFuture
25. When is it better to use CompletableFuture vs reactive programming
26. What does join() do and how does it differ from get()
27. Can you manually complete a CompletableFuture with a result
28. How to implement retry logic with CompletableFuture

### 20. Records and Generics (27 questions)
1. What is a Record in Java and since which version is it available
2. What are the main differences between Record and a regular class
3. Can you inherit from a Record or make a Record inherit from another class
4. Can you add additional methods to a Record
5. What methods are automatically generated for a Record
6. Can you override the constructor in a Record
7. What is a compact constructor in a Record
8. Can you declare static fields and methods in a Record
9. Are Record fields final
10. Can you use a Record as a key in HashMap
11. What are Generics in Java
12. What are the advantages of using generics
13. What is type erasure
14. Can you create an array of a generic type
15. What are bounded type parameters
16. Difference between extends T and super T
17. What is PECS (Producer Extends Consumer Super)
18. Can you use primitive types as generic parameters
19. What are raw types and why should you avoid them
20. What happens when you try to create an instance of a generic type via new T()
21. Difference between List<?> and List<Object>
22. Can you overload methods that differ only in generic parameters
23. What is a recursive type bound
24. How do generics work with inheritance
25. What are bridge methods and why are they needed
26. Can you use multiple bounds for a single type parameter
27. How to implement the Singleton pattern using a Record

---

## Quick Stats

| Category                             | Questions |
| ------------------------------------ | --------- |
| Databases SQL PostgreSQL             | 21        |
| Design Patterns                      | 16        |
| Memory and Garbage Collection        | 28        |
| Collections                          | 31        |
| Spring Spring Boot                   | 29        |
| REST HTTP                            | 30        |
| Exceptions                           | 28        |
| Stream API                           | 29        |
| Multithreading                       | 28        |
| HashMap equals hashCode              | 29        |
| Transactions                         | 22        |
| String                               | 23        |
| Immutability                         | 29        |
| Docker Kubernetes                    | 24        |
| Kafka                                | 30        |
| Hibernate JPA                        | 30        |
| Microservices                        | 26        |
| OOP and SOLID                        | 22        |
| CompletableFuture and Asynchronicity | 27        |
| Records and Generics                 | 27        |
| **Total**                            | **~500**  |

---

## Technologies Covered

- **Java:** 8, 11, 17, 21 (LTS versions)
- **Spring:** Spring Framework 6.x, Spring Boot 3.x
- **Databases:** PostgreSQL 15+, MySQL 8.0+
- **ORM:** Hibernate 6.x, JPA 3.1+
- **Infrastructure:** Docker 24+, Kubernetes 1.25+
- **Messaging:** Kafka 3.x

---

*Last updated: 2026-04-03*
