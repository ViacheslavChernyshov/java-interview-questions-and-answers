---
layout: default
title: Java Interview Questions та Відповіді - Портал підготовки до співбесід
description: Повна база з 500+ питань та відповідей для підготовки до співбесіди на Java Junior, Middle та Senior. Spring Boot, SQL, Hibernate, Kafka, Concurrency, Docker, Архітектура.
lang: uk
image: /assets/social-preview/github-social-preview.png
alternates:
  - lang: en
    url: /
  - lang: ru
    url: /ru/
  - lang: uk
    url: /uk/
  - lang: x-default
    url: /
---

<section class="hero-section">
  <div class="hero-badge">
    <span>☕ Портал підготовки до Java-інтерв'ю</span>
  </div>
  <h1 class="hero-title">500+ питань та відповідей для Java співбесіди</h1>
  <p class="hero-subtitle">Систематизована база знань з 20 ключових тем бекенду з 3-рівневими відповідями для Junior, Middle та Senior інженерів.</p>

  <div class="hero-search-box">
    <input type="text" class="hero-search-input" id="hero-search-input" placeholder="Пошук по 500+ питанням, темам та концепціям... (Ctrl+K)" readonly>
    <svg class="hero-search-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
  </div>

  <div class="stats-grid">
    <div class="stat-box">
      <span class="stat-value">507</span>
      <span class="stat-label">Питань та відповідей</span>
    </div>
    <div class="stat-box">
      <span class="stat-value">20</span>
      <span class="stat-label">Тематичних розділів</span>
    </div>
    <div class="stat-box">
      <span class="stat-value">3</span>
      <span class="stat-label">Рівні в кожній відповіді</span>
    </div>
    <div class="stat-box">
      <span class="stat-value">100%</span>
      <span class="stat-label">Open Source & Безкоштовно</span>
    </div>
  </div>
</section>

<div class="section-heading-wrap">
  <h2 class="section-main-title">20 тематичних розділів</h2>
  <p class="section-main-subtitle">Оберіть розділ, щоб відкрити структуровані відповіді з аналізом підкапотних механік та шпаргалками для інтерв'ю.</p>
</div>

<div class="topics-grid">
  <a class="topic-card" href="{{ '/uk/questions/01-databases-sql-postgresql/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🗄️</span>
      <span class="topic-count">21 питання</span>
    </div>
    <div>
      <h3 class="topic-title">1. Бази даних SQL PostgreSQL</h3>
      <p class="topic-desc">Індекси, B-Tree, MVCC, VACUUM, JOIN-и, віконні функції та оптимізація запитів.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/02-design-patterns/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🧩</span>
      <span class="topic-count">16 питань</span>
    </div>
    <div>
      <h3 class="topic-title">2. Патерни проектування</h3>
      <p class="topic-desc">Патерни GoF у Java: Singleton, Factory, Strategy, Observer, Decorator та Proxy.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/03-memory-and-garbage-collection/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🧠</span>
      <span class="topic-count">28 питань</span>
    </div>
    <div>
      <h3 class="topic-title">3. Пам'ять та Garbage Collection</h3>
      <p class="topic-desc">Будова JVM Heap, Stack, Metaspace, збирачі G1, ZGC, витоки пам'яті та OutOfMemoryError.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/04-collections/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">📦</span>
      <span class="topic-count">30 питань</span>
    </div>
    <div>
      <h3 class="topic-title">4. Колекції</h3>
      <p class="topic-desc">ArrayList, LinkedList, TreeSet, ConcurrentHashMap, fail-fast та fail-safe ітератори.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/05-spring-spring-boot/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🍃</span>
      <span class="topic-count">29 питань</span>
    </div>
    <div>
      <h3 class="topic-title">5. Spring Spring Boot</h3>
      <p class="topic-desc">IoC, DI, життєвий цикл бінів, BeanPostProcessor, автоконфігурація, актуатори та проксі.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/06-rest-http/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🌐</span>
      <span class="topic-count">17 питань</span>
    </div>
    <div>
      <h3 class="topic-title">6. REST HTTP</h3>
      <p class="topic-desc">HTTP-методи, ідемпотентність, коди статусу, модель зрілості REST та дизайн API.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/07-exceptions/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">⚡</span>
      <span class="topic-count">29 питань</span>
    </div>
    <div>
      <h3 class="topic-title">7. Винятки</h3>
      <p class="topic-desc">Checked vs Unchecked, try-with-resources, AutoCloseable, suppressed винятки та кращі практики.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/08-stream-api/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🌊</span>
      <span class="topic-count">29 питань</span>
    </div>
    <div>
      <h3 class="topic-title">8. Stream API</h3>
      <p class="topic-desc">Проміжні та термінальні операції, колектори, паралельні стріми, reduce, Spliterator.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/09-concurrency/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🧵</span>
      <span class="topic-count">27 питань</span>
    </div>
    <div>
      <h3 class="topic-title">9. Багатопоточність</h3>
      <p class="topic-desc">JMM, synchronized, volatile, CAS, Atomic-класи, ThreadPool, Virtual Threads та дедлоки.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/10-hashmap-equals-hashcode/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🔑</span>
      <span class="topic-count">29 питань</span>
    </div>
    <div>
      <h3 class="topic-title">10. HashMap equals hashCode</h3>
      <p class="topic-desc">Внутрішня будова бакетів, treeification (червоно-чорні дерева), колізії та контракти.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/11-transactions/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">💳</span>
      <span class="topic-count">22 питання</span>
    </div>
    <div>
      <h3 class="topic-title">11. Транзакції</h3>
      <p class="topic-desc">Властивості ACID, рівні ізоляції, propagation-стратегії у Spring `@Transactional` та 2PC.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/12-string/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🔤</span>
      <span class="topic-count">23 питання</span>
    </div>
    <div>
      <h3 class="topic-title">12. String</h3>
      <p class="topic-desc">String Pool, Compact Strings, StringBuilder vs StringBuffer, переваги імутабельності.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/13-immutability/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🔒</span>
      <span class="topic-count">29 питань</span>
    </div>
    <div>
      <h3 class="topic-title">13. Імутабельність</h3>
      <p class="topic-desc">Захисне копіювання, unmodifiable-обгортки, Java Records, потокобезпечність через незмінність.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/14-docker-kubernetes/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🐳</span>
      <span class="topic-count">24 питання</span>
    </div>
    <div>
      <h3 class="topic-title">14. Docker Kubernetes</h3>
      <p class="topic-desc">Контейнеризація, multi-stage збірка, Pods, Services, Deployments, ConfigMaps та Probes.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/15-kafka/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">📨</span>
      <span class="topic-count">30 питань</span>
    </div>
    <div>
      <h3 class="topic-title">15. Kafka</h3>
      <p class="topic-desc">Топіки, партиції, групи консьюмерів, семантики доставки, офсети, ідемпотентність та ребалансування.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/16-hibernate-jpa/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">💾</span>
      <span class="topic-count">30 питань</span>
    </div>
    <div>
      <h3 class="topic-title">16. Hibernate JPA</h3>
      <p class="topic-desc">Життєвий цикл сутностей, проблема N+1, стратегії fetch, L1/L2 кеші, оптимістичні блокування.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/17-microservices/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🏗️</span>
      <span class="topic-count">26 питань</span>
    </div>
    <div>
      <h3 class="topic-title">17. Мікросервіси</h3>
      <p class="topic-desc">Service Discovery, API Gateway, Circuit Breaker, патерн Saga, розподілений трейсинг, CQRS.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/18-oop-and-solid/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">📐</span>
      <span class="topic-count">22 питання</span>
    </div>
    <div>
      <h3 class="topic-title">18. ООП та SOLID</h3>
      <p class="topic-desc">Інкапсуляція, поліморфізм, успадкування проти композиції, принципи Single Responsibility, LSP, DIP.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/19-completablefuture-and-asynchrony/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">⏱️</span>
      <span class="topic-count">28 питань</span>
    </div>
    <div>
      <h3 class="topic-title">19. CompletableFuture та асинхронність</h3>
      <p class="topic-desc">Асинхронна композиція, обробка помилок, allOf / anyOf, керування пулами потоків.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/uk/questions/20-records-and-generics/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">📋</span>
      <span class="topic-count">27 питань</span>
    </div>
    <div>
      <h3 class="topic-title">20. Records та Дженерики</h3>
      <p class="topic-desc">Java Records, Type Erasure, Wildcards `? extends / super`, правило PECS, Bridge-методи.</p>
    </div>
    <div class="topic-footer">Почати підготовку →</div>
  </a>
</div>
