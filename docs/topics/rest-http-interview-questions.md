---
layout: default
title: REST and HTTP Interview Questions and Answers
description: REST and HTTP interview questions and answers about methods, idempotency, status codes, caching, pagination, versioning, authentication, and API design.
lang: en
image: /assets/social-preview/github-social-preview.png
---

<section class="hero">
  <span class="eyebrow">Topic Page</span>
  <h1>REST and HTTP interview questions and answers.</h1>
  <p class="lede">REST and HTTP questions are common in Java backend interviews because nearly every service exposes APIs. This page groups the API design and protocol fundamentals that help candidates explain not just how to build endpoints, but how to make them predictable, robust, and production-friendly.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ site.github.repository_url }}/blob/master/README.md#6-rest--http">Browse REST and HTTP section on GitHub</a>
    <a class="button" href="{{ '/' | relative_url }}">Back to home</a>
  </div>
</section>

<section class="section">
  <h2>What strong REST answers usually include</h2>
  <p>Interviewers often use API questions to measure clarity of thinking. Good answers show that you understand HTTP semantics, not just controller annotations. That includes choosing the right method, status code, and payload shape, as well as handling idempotency, caching, pagination, versioning, and error contracts consistently.</p>
  <p>These questions also connect nicely with Spring Boot, transactions, and security. A strong API designer can explain what the endpoint should do, how clients should interact with it, and what guarantees or failure modes the contract exposes.</p>
</section>

<section class="section">
  <h2>Representative REST and HTTP interview questions</h2>
  <ol class="topic-list">
    <li>What is REST and what are its core constraints?</li>
    <li>What is the difference between <code>PUT</code> and <code>PATCH</code>?</li>
    <li>What does idempotency mean in HTTP?</li>
    <li>Which HTTP status codes matter most for backend APIs?</li>
    <li>How should you design error responses?</li>
    <li>How do pagination and filtering usually work in REST APIs?</li>
    <li>What is content negotiation?</li>
    <li>How does HTTP caching work with headers such as <code>Cache-Control</code> and <code>ETag</code>?</li>
    <li>How should API versioning be handled?</li>
    <li>What is the difference between authentication and authorization in API design?</li>
  </ol>
</section>

<section class="section">
  <h2>Related pages</h2>
  <div class="card-grid">
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/spring-boot-interview-questions/' | relative_url }}">Spring Boot interview questions</a></h3>
      <p>Natural companion page because many Java API interviews are framed through Spring controllers and service layers.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/sql-postgresql-interview-questions/' | relative_url }}">SQL and PostgreSQL interview questions</a></h3>
      <p>Useful when API design discussions move into filtering, pagination, and data access performance.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/kafka-interview-questions/' | relative_url }}">Kafka interview questions</a></h3>
      <p>Helpful when the system mixes request-response APIs with asynchronous event processing.</p>
    </article>
  </div>
</section>
