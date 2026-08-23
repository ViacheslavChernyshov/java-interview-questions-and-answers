---
layout: default
title: Java Interview Questions и Ответы - Портал подготовки к собеседованиям
description: Полная база из 500+ вопросов и ответов для подготовки к собеседованию на Java Junior, Middle и Senior. Spring Boot, SQL, Hibernate, Kafka, Concurrency, Docker, Архитектура.
lang: ru
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
    <span>☕ Портал подготовки к Java-интервью</span>
  </div>
  <h1 class="hero-title">500+ вопросов и ответов для Java собеседования</h1>
  <p class="hero-subtitle">Систематизированная база знаний по 20 ключевым темам бэкенда с 3-уровневыми ответами для Junior, Middle и Senior инженеров.</p>

  <div class="hero-search-box">
    <input type="text" class="hero-search-input" id="hero-search-input" placeholder="Поиск по 500+ вопросам, темам и концепциям... (Ctrl+K)" readonly>
    <svg class="hero-search-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
  </div>

  <div class="stats-grid">
    <div class="stat-box">
      <span class="stat-value">507</span>
      <span class="stat-label">Вопросов и ответов</span>
    </div>
    <div class="stat-box">
      <span class="stat-value">20</span>
      <span class="stat-label">Тематических разделов</span>
    </div>
    <div class="stat-box">
      <span class="stat-value">3</span>
      <span class="stat-label">Уровня в каждом ответе</span>
    </div>
    <div class="stat-box">
      <span class="stat-value">100%</span>
      <span class="stat-label">Open Source & Бесплатно</span>
    </div>
  </div>
</section>

<div class="section-heading-wrap">
  <h2 class="section-main-title">20 тематических разделов</h2>
  <p class="section-main-subtitle">Выберите интересующий раздел, чтобы изучить подробные разборы с глубокими объяснениями и шпаргалками для интервью.</p>
</div>

<div class="topics-grid">
  <a class="topic-card" href="{{ '/ru/questions/01-databases-sql-postgresql/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🗄️</span>
      <span class="topic-count">21 вопрос</span>
    </div>
    <div>
      <h3 class="topic-title">1. Базы данных SQL PostgreSQL</h3>
      <p class="topic-desc">Индексы, B-Tree, MVCC, VACUUM, JOIN-ы, оконные функции и оптимизация запросов.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/02-design-patterns/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🧩</span>
      <span class="topic-count">16 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">2. Паттерны проектирования</h3>
      <p class="topic-desc">Паттерны GoF в Java: Singleton, Factory, Strategy, Observer, Decorator и Proxy.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/03-memory-and-garbage-collection/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🧠</span>
      <span class="topic-count">28 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">3. Память и Garbage Collection</h3>
      <p class="topic-desc">Устройство JVM Heap, Stack, Metaspace, сборщики G1, ZGC, утечки памяти и OutOfMemoryError.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/04-collections/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">📦</span>
      <span class="topic-count">30 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">4. Коллекции</h3>
      <p class="topic-desc">ArrayList, LinkedList, TreeSet, ConcurrentHashMap, fail-fast и fail-safe итераторы.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/05-spring-spring-boot/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🍃</span>
      <span class="topic-count">29 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">5. Spring Spring Boot</h3>
      <p class="topic-desc">IoC, DI, жизненный цикл бинов, BeanPostProcessor, автоконфигурация, актуаторы и прокси.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/06-rest-http/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🌐</span>
      <span class="topic-count">17 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">6. REST HTTP</h3>
      <p class="topic-desc">HTTP-методы, идемпотентность, коды состояния, модель зрелости REST и дизайн API.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/07-exceptions/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">⚡</span>
      <span class="topic-count">29 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">7. Исключения</h3>
      <p class="topic-desc">Checked vs Unchecked, try-with-resources, AutoCloseable, suppressed исключения и лучшие практики.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/08-stream-api/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🌊</span>
      <span class="topic-count">29 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">8. Stream API</h3>
      <p class="topic-desc">Промежуточные и терминальные операции, коллекторы, параллельные стримы, reduce, Spliterator.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/09-concurrency/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🧵</span>
      <span class="topic-count">27 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">9. Многопоточность</h3>
      <p class="topic-desc">JMM, synchronized, volatile, CAS, Atomic-классы, ThreadPool, Virtual Threads и дедлоки.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/10-hashmap-equals-hashcode/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🔑</span>
      <span class="topic-count">29 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">10. HashMap equals hashCode</h3>
      <p class="topic-desc">Внутреннее устройство бакетов, treeification (красно-черные деревья), коллизии и контракты.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/11-transactions/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">💳</span>
      <span class="topic-count">22 вопроса</span>
    </div>
    <div>
      <h3 class="topic-title">11. Транзакции</h3>
      <p class="topic-desc">Свойства ACID, уровни изоляции, propagation-стратегии в Spring `@Transactional` и 2PC.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/12-string/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🔤</span>
      <span class="topic-count">23 вопроса</span>
    </div>
    <div>
      <h3 class="topic-title">12. String</h3>
      <p class="topic-desc">String Pool, Compact Strings, StringBuilder vs StringBuffer, преимущества иммутабельности.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/13-immutability/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🔒</span>
      <span class="topic-count">29 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">13. Иммутабельность</h3>
      <p class="topic-desc">Защитное копирование, unmodifiable-обертки, Java Records, потокобезопасность через неизменяемость.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/14-docker-kubernetes/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🐳</span>
      <span class="topic-count">24 вопроса</span>
    </div>
    <div>
      <h3 class="topic-title">14. Docker Kubernetes</h3>
      <p class="topic-desc">Контейнеризация, multi-stage сборка, Pods, Services, Deployments, ConfigMaps и Probes.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/15-kafka/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">📨</span>
      <span class="topic-count">30 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">15. Kafka</h3>
      <p class="topic-desc">Топики, партиции, группы консьюмеров, семантики доставки, оффсеты, идемпотентность и ребалансировка.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/16-hibernate-jpa/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">💾</span>
      <span class="topic-count">30 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">16. Hibernate JPA</h3>
      <p class="topic-desc">Жизненный цикл сущностей, проблема N+1, стратегии fetch, L1/L2 кэши, оптимистичные блокировки.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/17-microservices/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">🏗️</span>
      <span class="topic-count">26 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">17. Микросервисы</h3>
      <p class="topic-desc">Service Discovery, API Gateway, Circuit Breaker, паттерн Saga, распределенный трейсинг, CQRS.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/18-oop-and-solid/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">📐</span>
      <span class="topic-count">22 вопроса</span>
    </div>
    <div>
      <h3 class="topic-title">18. ООП и SOLID</h3>
      <p class="topic-desc">Инкапсуляция, полиморфизм, наследование против композиции, принципы Single Responsibility, LSP, DIP.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/19-completablefuture-and-asynchrony/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">⏱️</span>
      <span class="topic-count">28 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">19. CompletableFuture и асинхронность</h3>
      <p class="topic-desc">Асинхронная композиция, обработка ошибок, allOf / anyOf, управление пулами потоков.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>

  <a class="topic-card" href="{{ '/ru/questions/20-records-and-generics/' | relative_url }}">
    <div class="topic-card-top">
      <span class="topic-icon">📋</span>
      <span class="topic-count">27 вопросов</span>
    </div>
    <div>
      <h3 class="topic-title">20. Records и Дженерики</h3>
      <p class="topic-desc">Java Records, Type Erasure, Wildcards `? extends / super`, правило PECS, Bridge-методы.</p>
    </div>
    <div class="topic-footer">Начать подготовку →</div>
  </a>
</div>
