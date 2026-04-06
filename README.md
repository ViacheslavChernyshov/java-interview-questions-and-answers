# Java Developer Interview Questions

## 🇬🇧 English

A comprehensive collection of **516 interview questions** for Middle Java Developer position, organized into **20 topic categories**. Each question has a detailed answer structured across three levels: 🟢 Junior, 🟡 Middle, 🔴 Senior.

---

## 📚 Table of Contents

| #   | Topic                                                               | Questions   |
| --- | ------------------------------------------------------------------- | ----------- |
| 20  | [Records & Generics](#20-records--generics)                         | 27          |
| 19  | [CompletableFuture & Asynchrony](#19-completableFuture--asynchrony) | 28          |
| 18  | [OOP & SOLID](#18-oop--solid)                                       | 22          |
| 17  | [Microservices](#17-microservices)                                  | 26          |
| 16  | [Hibernate / JPA](#16-hibernate--jpa)                               | 30          |
| 15  | [Kafka](#15-kafka)                                                  | 30          |
| 14  | [Docker / Kubernetes](#14-docker--kubernetes)                       | 24          |
| 13  | [Immutability](#13-immutability)                                    | 29          |
| 12  | [String](#12-string)                                                | 23          |
| 11  | [Transactions](#11-transactions)                                    | 22          |
| 10  | [HashMap / equals / hashCode](#10-hashmap--equals--hashcode)        | 29          |
| 9   | [Concurrency](#9-concurrency)                                       | 27          |
| 8   | [Stream API](#8-stream-api)                                         | 29          |
| 7   | [Exceptions](#7-exceptions)                                         | 29          |
| 6   | [REST / HTTP](#6-rest--http)                                        | 17          |
| 5   | [Spring / Spring Boot](#5-spring--spring-boot)                      | 29          |
| 4   | [Collections](#4-collections)                                       | 30          |
| 3   | [Memory & Garbage Collection](#3-memory--garbage-collection)        | 28          |
| 2   | [Design Patterns](#2-design-patterns)                               | 16          |
| 1   | [Databases / SQL / PostgreSQL](#1-databases--sql--postgresql)       | 21          |

---

## 20. Records & Generics

1. What is Record in Java and since which version is it available?
2. What are the main differences between Record and a regular class?
3. Can you inherit from Record or extend Record from another class?
4. Can you add additional methods to Record?
5. Which methods are automatically generated for Record?
6. Can you override the constructor in Record?
7. What is a compact constructor in Record?
8. Can you declare static fields and methods in Record?
9. Are Record fields final?
10. Can you use Record as a key in HashMap?
11. What are Generics in Java?
12. What are the advantages of using generics?
13. What is type erasure?
14. Can you create an array of generic type?
15. What are bounded type parameters?
16. What is the difference between `<? extends T>` and `<? super T>`?
17. What is PECS (Producer Extends Consumer Super)?
18. Can you use primitive types as generic parameters?
19. What are raw types and why should you avoid them?
20. What happens when you try to create an instance of generic type via `new T()`?
21. What is the difference between `List<?>` and `List<Object>`?
22. Can you overload methods differing only by generic parameters?
23. What is recursive type bound?
24. How do generics work with inheritance (is `List<String>` a subtype of `List<Object>`)?
25. What are bridge methods and why are they needed?
26. Can you use multiple bounds for a single type parameter?
27. How to implement Singleton pattern using Record?

## 19. CompletableFuture & Asynchrony

28. What is CompletableFuture and how does it differ from Future?
29. What are the main advantages of CompletableFuture over Future?
30. How to create a CompletableFuture that is already completed with a result?
31. What is the difference between thenApply() and thenCompose()?
32. What do methods thenAccept() and thenRun() do?
33. How to handle exceptions in a CompletableFuture chain?
34. What is the difference between handle(), exceptionally() and whenComplete()?
35. How to combine results of multiple CompletableFutures?
36. What does allOf() method do and when to use it?
37. What does anyOf() method do and in which cases is it useful?
38. What is the difference between thenApply() and thenApplyAsync()?
39. What thread pool is used by default for async methods?
40. How to specify your own Executor for CompletableFuture?
41. What is blocking code and how to distinguish it from non-blocking?
42. Why is it important to avoid blocking operations in CompletableFuture?
43. How to properly execute multiple parallel requests to microservices?
44. What does supplyAsync() method do and when to use it?
45. How to cancel CompletableFuture execution?
46. What happens if an exception occurs in a CompletableFuture chain?
47. Can you reuse the same CompletableFuture in multiple chains?
48. How to implement timeout for CompletableFuture?
49. What does orTimeout() method do in Java 9+?
50. What is the difference between thenCombine() and thenCompose()?
51. How to test code with CompletableFuture?
52. When is it better to use CompletableFuture vs reactive programming?
53. What does join() method do and how does it differ from get()?
54. Can you manually complete a CompletableFuture with a result?
55. How to implement retry logic with CompletableFuture?

## 18. OOP & SOLID

56. What is the Single Responsibility Principle and how to apply it?
57. Give an example of Single Responsibility Principle violation.
58. What is the Open/Closed Principle?
59. How to refactor code that violates Open/Closed Principle?
60. What is the Liskov Substitution Principle?
61. Give an example of Liskov Substitution Principle violation.
62. What is the Interface Segregation Principle?
63. What is the Dependency Inversion Principle?
64. Why do we need SOLID principles at all?
65. What are composition and inheritance?
66. When is it better to use composition instead of inheritance?
67. What is delegation in OOP?
68. How is Single Responsibility Principle related to cohesion?
69. What happens if a class has multiple reasons to change?
70. How does SOLID help with code testing?
71. How is Dependency Inversion related to Dependency Injection?
72. What is Law of Demeter (principle of least knowledge)?
73. How to refactor a God Object?
74. How do SOLID principles help with feature extension?
75. Can you follow all SOLID principles simultaneously?
76. How to determine that a class has a single responsibility?
77. What anti-patterns contradict SOLID principles?

## 17. Microservices

78. What is the Saga pattern and when to use it?
79. What is the difference between choreography and orchestration in Saga?
80. How to implement distributed transactions in microservices?
81. What are compensating transactions?
82. What is the Circuit Breaker pattern?
83. How does Circuit Breaker work and what states does it have?
84. What is Service Discovery and why is it needed?
85. What is the difference between client-side and server-side discovery?
86. What is API Gateway and what tasks does it solve?
87. What is sharding?
88. What is the difference between sharding and partitioning?
89. How to implement horizontal scaling of microservices?
90. What is the Database per Service pattern?
91. What problems arise when using a shared database?
92. How to organize communication between microservices?
93. What is the difference between synchronous and asynchronous communication?
94. How to ensure fault tolerance of microservices?
95. What is the Bulkhead pattern?
96. What is the Retry pattern and how to use it properly?
97. What is exponential backoff?
98. How to monitor a distributed microservice system?
99. What is distributed tracing?
100. How to implement authentication and authorization in microservices?
101. What is the Strangler Fig pattern?
102. How to test microservices?
103. What tools are used for microservice orchestration?

## 16. Hibernate / JPA

104. What is the N+1 problem and how to solve it?
105. What is the difference between Lazy and Eager loading?
106. When to use Lazy vs Eager loading?
107. What is LazyInitializationException and how to avoid it?
108. What fetch strategies exist in Hibernate?
109. What does @BatchSize annotation do?
110. Describe the Entity lifecycle in Hibernate.
111. What are states: transient, persistent, detached, removed?
112. What is the first-level cache in Hibernate?
113. What is the second-level cache and when to use it?
114. How to configure the second-level cache?
115. What is dirty checking in Hibernate?
116. How does the flush mechanism work in Hibernate?
117. What is the difference between persist() and merge()?
118. What does the refresh() method do?
119. What is EntityManager and how does it differ from Session?
120. How to implement optimistic locking in JPA?
121. How to implement pessimistic locking in JPA?
122. What is @Version and why is it needed?
123. How do cascade operations (Cascade) work?
124. What types of Cascade exist?
125. What is orphan removal?
126. How to properly use @OneToMany and @ManyToOne?
127. What are the peculiarities of bidirectional relationships?
128. How to avoid infinite recursion during Entity serialization?
129. What is JPQL and how does it differ from SQL?
130. What is Criteria API and when to use it?
131. How to use JOIN FETCH to solve the N+1 problem?
132. What is projection in JPA?
133. What types of inheritance does JPA support?

## 15. Kafka

134. What is a topic in Kafka?
135. What is a partition and why is it needed?
136. How is data distributed across partitions?
137. What is a message key and how does it affect partitioning?
138. What is a Consumer Group?
139. How does consumer load balancing work within a group?
140. Can you have more consumers than partitions?
141. What happens when a new consumer is added to a group?
142. What delivery guarantees does Kafka provide?
143. What is the difference between at-most-once, at-least-once and exactly-once?
144. How to configure exactly-once semantics?
145. What is an offset in Kafka?
146. How does commit offset work?
147. What is the difference between auto commit and manual commit?
148. What is rebalancing and when does it happen?
149. What is replication in Kafka?
150. What are leader and follower replicas?
151. What is ISR (In-Sync Replicas)?
152. How does Kafka ensure fault tolerance?
153. What is producer acknowledgment and what modes exist (acks=0,1,all)?
154. What is a batch in Kafka producer?
155. How does message compression work?
156. What is an idempotent producer?
157. How to handle errors when reading messages?
158. What is DLQ (Dead Letter Queue)?
159. How to monitor consumer lag?
160. What is a retention policy?
161. How are old messages deleted from a topic?
162. Can you read messages from a specific partition?
163. How to implement message filtering on the consumer side?

## 14. Docker / Kubernetes

164. What is containerization and why is it needed?
165. What is the difference between a container and a virtual machine?
166. What is a Dockerfile?
167. What are the main instructions used in a Dockerfile?
168. What is the difference between CMD and ENTRYPOINT?
169. What is multi-stage build?
170. What is Docker Compose?
171. What is Kubernetes and why is it needed?
172. What is a Pod in Kubernetes?
173. What is a Node in Kubernetes?
174. What is a Service in Kubernetes?
175. What types of Service exist (ClusterIP, NodePort, LoadBalancer)?
176. What is a ReplicaSet?
177. How does scaling work in Kubernetes?
178. What is HorizontalPodAutoscaler?
179. What is the difference between ConfigMap and Secret?
180. What is a liveness probe?
181. What is a readiness probe?
182. Why are health checks needed?
183. What is Ingress in Kubernetes?
184. What is a namespace?
185. How to organize a rolling update in Kubernetes?
186. What is a StatefulSet and when to use it?
187. How to monitor applications in Kubernetes?

## 13. Immutability

188. What is an immutable (unchangeable) object?
189. What advantages do immutable objects provide?
190. How to create an immutable class in Java?
191. Why is the String class immutable?
192. What are the consequences of String immutability?
193. Why are immutable objects thread-safe?
194. What is the `final` keyword and how does it help create immutable classes?
195. Is making all fields final sufficient for immutability?
196. What to do if a class field references a mutable object?
197. What is a defensive copy?
198. When do you need to make a defensive copy?
199. How to protect a collection from modifications?
200. What is Collections.unmodifiableList() and how does it work?
201. What is the difference between shallow copy and deep copy?
202. Can you inherit from an immutable class?
203. Why must an immutable class be final?
204. What happens if you override a getter in a subclass of an immutable class?
205. How does String pool work and how is it related to immutability?
206. Can you change a String value via reflection?
207. What is Record and how does it help create immutable classes?
208. Why are LocalDate and LocalDateTime immutable?
209. What are the advantages of immutable objects for caching?
210. How does immutability affect performance?
211. What are persistent data structures?
212. Are there any disadvantages to immutable objects?
213. How to implement Builder pattern for an immutable class?
214. Can you use immutable objects as keys in HashMap?
215. What happens if you change a mutable key in HashMap?
216. How to properly work with collections in immutable classes?

## 12. String

217. How does String Pool work?
218. What is the difference between creating a String via literal and via `new`?
219. When should you use intern()?
220. Why is String immutable?
221. When to use StringBuilder vs StringBuffer?
222. Why is StringBuffer slower than StringBuilder?
223. What happens when concatenating strings via the `+` operator?
224. How does the Java compiler optimize string concatenation?
225. Can you use `==` to compare Strings?
226. What is the difference between `==` and equals() for String?
227. Where is the String Pool stored (in which memory area)?
228. Can String Pool cause OutOfMemoryError?
229. What does the substring() method do and how did it work before Java 7?
230. Why was the substring() implementation changed in Java 7?
231. How does the split() method work?
232. What is the difference between replace() vs replaceAll()?
233. What is String encoding?
234. How to properly convert a String to byte[] and back?
235. What are compact strings in Java 9+?
236. How to find out how much memory a String occupies?
237. Can you change the content of a String via reflection?
238. What is String deduplication in G1 GC?
239. Why does String implement Comparable and CharSequence?

## 11. Transactions

240. Decode each letter of ACID.
241. What transaction isolation levels exist?
242. What is Read Uncommitted?
243. What is Read Committed?
244. What is Repeatable Read?
245. What is Serializable?
246. What is a dirty read?
247. What is a non-repeatable read?
248. What is a phantom read?
249. What is a lost update?
250. What is the default isolation level in PostgreSQL?
251. What is the default isolation level in MySQL?
252. What is Propagation in Spring?
253. What does Propagation.NESTED do?
254. What is the difference between REQUIRED and REQUIRES_NEW?
255. What is the @Transactional annotation?
256. At which level can you use @Transactional?
257. What is rollback in transactions?
258. Which exceptions trigger rollback by default?
259. How to configure rollback for checked exceptions?
260. What is a readonly transaction?
261. What happens when you call a @Transactional method from another method of the same class?

## 10. HashMap / equals / hashCode

262. How is HashMap structured internally?
263. What is a bucket in HashMap?
264. How does HashMap determine which bucket to put an element in?
265. What is a collision in HashMap?
266. How does HashMap handle collisions?
267. What happens when 8 elements are reached in one bucket?
268. What is the equals() and hashCode() contract?
269. If two objects are equal by equals(), what can you say about their hashCode()?
270. If two objects have the same hashCode(), are they necessarily equal by equals()?
271. What happens if you override equals() but not hashCode()?
272. What happens if you override hashCode() but not equals()?
273. Can you use a mutable object as a key in HashMap?
274. What happens if you change a key after adding it to HashMap?
275. What are the requirements for a HashMap key?
276. Why is String often used as a key in HashMap?
277. What is load factor in HashMap?
278. What is capacity in HashMap?
279. When does rehashing occur in HashMap?
280. What happens during rehashing?
281. What is the time complexity of get() and put() operations in HashMap?
282. When can the time complexity become O(n)?
283. How does HashMap work in a multi-threaded environment?
284. What is ConcurrentHashMap and how does it differ from HashMap?
285. Can you store a null key in HashMap?
286. Can you store a null value in HashMap?
287. What is the difference between HashMap and Hashtable?
288. What is WeakHashMap?
289. How to properly choose initial capacity for HashMap?
290. Which is better: ArrayList or HashMap for storing key-value pairs?

## 9. Concurrency

291. What is the difference between synchronized and volatile?
292. What is happens-before relationship?
293. What is the visibility problem?
294. What is a monitor in Java?
295. How does synchronized work at the monitor level?
296. What is the difference between a synchronized method and a synchronized block?
297. What is a reentrant lock?
298. What are Atomic classes?
299. What is CAS (Compare-And-Swap)?
300. How do AtomicInteger and AtomicLong work?
301. What are the advantages of Atomic classes over synchronized?
302. What is a Thread Pool?
303. What types of Thread Pool exist in Java?
304. What does ExecutorService do?
305. What is the difference between Executors.newFixedThreadPool() and newCachedThreadPool()?
306. What is ForkJoinPool?
307. What is a deadlock?
308. What conditions are necessary for a deadlock to occur?
309. How to prevent deadlock?
310. What is a race condition?
311. How to avoid race conditions?
312. What are Virtual Threads in Java 21?
313. What are the advantages of Virtual Threads over regular threads?
314. When should you use Virtual Threads?
315. What is structured concurrency?
316. What is the difference between Thread and Runnable?
317. What are Callable and Future?

## 8. Stream API

318. What advantages does Stream API provide?
319. What is the difference between intermediate and terminal operations?
320. What does the filter() operation do?
321. What does the map() operation do?
322. What does the collect() operation do?
323. What is a Collector and what built-in Collectors exist?
324. What does the flatMap() operation do?
325. What is the difference between map() and flatMap()?
326. What are parallel streams?
327. When to use parallel streams?
328. How to create a parallel stream?
329. What potential problems can arise with parallel streams?
330. What is ForkJoinPool and how is it related to parallel streams?
331. Can you modify the state of external variables in Stream operations?
332. What are side effects in Stream?
333. Why should you avoid side effects in Stream?
334. What does the reduce() operation do?
335. What is the difference between reduce() and collect()?
336. What is the peek() operation and when to use it?
337. Can you reuse a Stream?
338. What is lazy evaluation in Stream?
339. When does the execution of Stream operations begin?
340. What do distinct(), sorted(), limit(), skip() operations do?
341. How does short-circuiting work in Stream?
342. What are anyMatch(), allMatch(), noneMatch() operations?
343. What do findFirst() and findAny() operations do?
344. How to collect a Stream into a Map?
345. What to do with key collisions when collecting into a Map?
346. How to work with Optional in Stream?

## 7. Exceptions

347. What is the difference between checked and unchecked exceptions?
348. What is a checked exception and when to use it?
349. What is an unchecked exception (Runtime Exception)?
350. Which exceptions must always be handled?
351. What is at the top of the exception hierarchy?
352. What is Throwable?
353. What is the difference between Error and Exception?
354. Is the finally block guaranteed to execute?
355. What is try-with-resources?
356. What are the requirements for resources in try-with-resources?
357. What is the AutoCloseable interface?
358. What is the difference between AutoCloseable and Closeable?
359. Can you create custom exceptions?
360. When should you create your own exceptions?
361. Which is better: extending Exception or RuntimeException?
362. What is a stack trace?
363. What does the printStackTrace() method do?
364. How to properly log exceptions?
365. What is exception wrapping?
366. Why shouldn't you swallow exceptions (empty catch)?
367. What does the throws keyword do?
368. Can you throw a checked exception from a method without throws?
369. What happens if an exception also occurs in the finally block?
370. What are suppressed exceptions?
371. Can you have multiple catch blocks for a single try?
372. What is multi-catch?
373. In what order should you arrange catch blocks?
374. Can you re-throw an exception?
375. What is exception chaining?

## 6. REST / HTTP

376. What is REST?
377. What does Stateless mean in the context of REST?
378. What are the main HTTP methods used in REST?
379. What is the difference between PUT and PATCH?
380. What is idempotency?
381. Which HTTP methods are idempotent?
382. Why are GET and DELETE idempotent?
383. Is POST idempotent?
384. What HTTP status codes do you know?
385. What is the difference between 401 and 403?
386. What is RESTful API design?
387. How to properly name REST endpoints?
388. Should you use verbs in URLs?
389. What is HATEOAS?
390. How to organize REST API versioning?
391. What is the Content-Type header?
392. What is the Accept header?

## 5. Spring / Spring Boot

393. What is Dependency Injection?
394. What is the difference between constructor, setter and field injection?
395. Which injection type is recommended and why?
396. What is a Bean in Spring?
397. How to create a Bean in Spring?
398. What is Bean Lifecycle?
399. What are the stages of Bean lifecycle?
400. What is BeanPostProcessor?
401. What do methods with @PostConstruct and @PreDestroy annotations do?
402. What is Bean scope?
403. What scopes exist in Spring?
404. What is the difference between singleton and prototype scope?
405. What is a proxy in Spring?
406. When does Spring create a proxy?
407. What is AOP (Aspect-Oriented Programming)?
408. What are aspect, advice, pointcut, join point?
409. What does the @Transactional annotation do?
410. Why doesn't @Transactional work with self-invocation?
411. How to solve the self-invocation problem?
412. What is auto-configuration in Spring Boot?
413. How does @SpringBootApplication work?
414. What is a starter in Spring Boot?
415. What does the @ComponentScan annotation do?
416. What is a @Configuration class?
417. What is the difference between @Component, @Service, @Repository, @Controller?
418. What does the @Autowired annotation do?
419. What to do if there are multiple beans of the same type?
420. What is @Qualifier?
421. What are profiles in Spring?

## 4. Collections

422. What are the main interfaces of the Collection Framework?
423. What is the difference between List, Set and Queue?
424. What is the difference between ArrayList and LinkedList?
425. When to use ArrayList vs LinkedList?
426. What is the time complexity of operations in ArrayList?
427. What is the time complexity of operations in LinkedList?
428. What is Vector and how does it differ from ArrayList?
429. What is Stack?
430. What is Queue and what implementations exist?
431. What is Deque?
432. What is the difference between HashSet, LinkedHashSet and TreeSet?
433. How does HashSet work internally?
434. What is TreeSet and how does it work?
435. What is Map and what implementations exist?
436. What is the difference between HashMap, LinkedHashMap and TreeMap?
437. When to use TreeMap?
438. What is WeakHashMap?
439. What is ConcurrentHashMap?
440. How does ConcurrentHashMap ensure thread-safety?
441. What is CopyOnWriteArrayList?
442. When to use synchronized collections?
443. How to get a synchronized collection?
444. What is Collections.unmodifiableList() and how does it work?
445. What is the difference between Iterator and ListIterator?
446. What are fail-fast and fail-safe iterators?
447. What is ConcurrentModificationException?
448. How to properly remove elements during iteration?
449. What are Comparable and Comparator?
450. What is the difference between Comparable and Comparator?
451. What operations does the Collection interface support?

## 3. Memory & Garbage Collection

452. What is the difference between Heap and Stack?
453. What is stored in Heap?
454. What is stored in Stack?
455. What is Garbage Collection?
456. When does an object become a candidate for GC removal?
457. What is a memory leak in Java?
458. How can a memory leak occur in Java?
459. What are generations in GC (young, old, metaspace)?
460. What is Young Generation?
461. What is Old Generation (Tenured)?
462. What is Metaspace (or PermGen)?
463. What GC algorithms exist?
464. What is G1 GC?
465. What is ZGC?
466. What is Shenandoah GC?
467. What is stop-the-world?
468. Which GCs minimize stop-the-world pauses?
469. What are the -Xms and -Xmx parameters?
470. What happens on OutOfMemoryError?
471. What types of OutOfMemoryError exist?
472. What is a memory leak and how to detect it?
473. What tools help analyze memory?
474. What is a heap dump?
475. How to get a heap dump?
476. What are GC roots?
477. What is reachability in the context of GC?
478. Can you manually invoke GC?
479. Why shouldn't you call System.gc()?

## 2. Design Patterns

480. What are design patterns?
481. What categories of patterns exist?
482. What is Singleton?
483. How to implement a thread-safe Singleton?
484. What is double-checked locking?
485. What are the problems with Singleton?
486. What is the difference between Factory Method and Abstract Factory?
487. When to use Builder?
488. What is the Prototype pattern?
489. When to use Strategy?
490. How is Observer implemented in Java?
491. What is the advantage of Decorator over inheritance?
492. What is the difference between State and Strategy?
493. What types of Proxy exist?
494. What is the Iterator pattern?
495. What anti-patterns do you know?

## 1. Databases / SQL / PostgreSQL

496. Why are indexes needed?
497. How does a B-tree index work?
498. What is a composite index?
499. When should you create an index?
500. What are the disadvantages of indexes?
501. What is index cardinality?
502. What types of JOIN exist?
503. What is the difference between INNER JOIN and LEFT JOIN?
504. Which is better: JOIN or subquery?
505. What is a correlated subquery?
506. What is the difference between WHERE and HAVING?
507. What does GROUP BY do?
508. When to use HAVING?
509. What are window functions?
510. What does ROW_NUMBER() do?
511. What do RANK() and DENSE_RANK() do?
512. How does MVCC work in PostgreSQL?
513. What is VACUUM in PostgreSQL?
514. Why is ANALYZE needed?
515. What is explain plan?
516. How to optimize slow queries?

---

## 📊 Statistics

| Metric               | Value                          |
| -------------------- | ------------------------------ |
| **Total questions**  | 516                            |
| **Total categories** | 20                             |
| **Each answer has**  | 🟢 Junior + 🟡 Middle + 🔴 Senior |
| **Language**         | Russian (🇷🇺)                   |

---

## 📂 Folder Structure

```
ru/
├── 1. Базы данных SQL PostgreSQL/          (21 files)
├── 2. Паттерны проектирования/             (16 files)
├── 3. Память и Garbage Collection/         (28 files)
├── 4. Коллекции/                           (30 files)
├── 5. Spring Spring Boot/                  (29 files)
├── 6. REST HTTP/                           (17 files)
├── 7. Исключения/                          (29 files)
├── 8. Stream API/                          (29 files)
├── 9. Многопоточность/                     (27 files)
├── 10. HashMap equals hashCode/            (29 files)
├── 11. Транзакции/                         (22 files)
├── 12. String/                             (23 files)
├── 13. Иммутабельность/                    (29 files)
├── 14. Docker Kubernetes/                  (24 files)
├── 15. Kafka/                              (30 files)
├── 16. Hibernate JPA/                      (30 files)
├── 17. Микросервисы/                       (26 files)
├── 18. ООП и SOLID/                        (22 files)
├── 19. CompletableFuture и асинхронность/  (28 files)
└── 20. Records и Дженерики/                (27 files)
```

---

## 🇷🇺 Русская версия

Полная русская версия с перечнем тем и вопросов находится в файле [INDEX.md](ru/INDEX.md).

Каждый файл содержит ответы трёх уровней сложности:
- 🟢 **Junior** — простые объяснения, базовые концепции
- 🟡 **Middle** — внутреннее устройство, типичные ошибки, практические нюансы
- 🔴 **Senior** — глубокие техническиекие детали, архитектурные решения, production-опыт

---

*Generated: 2026-04-03*
