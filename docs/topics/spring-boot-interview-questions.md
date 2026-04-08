---
layout: default
title: Spring Boot Interview Questions and Answers
description: Spring Boot interview questions and answers covering dependency injection, bean lifecycle, scopes, AOP, @Transactional, profiles, and Spring Boot internals.
lang: en
image: /assets/social-preview/github-social-preview.png
---

<section class="hero">
  <span class="eyebrow">Topic Page</span>
  <h1>Spring Boot interview questions and answers.</h1>
  <p class="lede">This topic page groups Spring Boot interview questions that show up often in backend interviews: dependency injection, bean lifecycle, proxies, AOP, transactional boundaries, configuration, and runtime behavior. It works best as a guided starting point before opening the full markdown repository.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ site.github.repository_url }}/blob/master/README.md#5-spring--spring-boot">Browse Spring section on GitHub</a>
    <a class="button" href="{{ '/' | relative_url }}">Back to home</a>
  </div>
</section>

<section class="section">
  <h2>What this Spring Boot section includes</h2>
  <p>The Spring material in this repository focuses on the questions that reveal whether a candidate understands how the framework really works, not just how to copy annotations from examples. Interviewers often test constructor injection, bean creation, autoconfiguration, proxies, scopes, and transactional behavior because those topics separate surface familiarity from production understanding.</p>
  <p>That means a strong Spring Boot preparation flow should not stop at definitions. You should be able to explain what happens during container startup, why self-invocation breaks some proxy-based features, when to use qualifiers, and how profiles or configuration classes change runtime behavior.</p>
</section>

<section class="section">
  <h2>Representative Spring Boot interview questions</h2>
  <ol class="topic-list">
    <li>What is dependency injection and why is it useful?</li>
    <li>What is a Bean in Spring and how is it created?</li>
    <li>What stages exist in the Bean lifecycle?</li>
    <li>What is the difference between constructor, setter, and field injection?</li>
    <li>What does <code>@Autowired</code> do and how should it be used?</li>
    <li>What does <code>@Transactional</code> do?</li>
    <li>Why can <code>@Transactional</code> fail during self-invocation?</li>
    <li>What is a proxy in Spring and when does Spring create one?</li>
    <li>How does <code>@SpringBootApplication</code> work?</li>
    <li>What are Spring profiles and when should you use them?</li>
  </ol>
</section>

<section class="section">
  <h2>Related pages</h2>
  <div class="card-grid">
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/sql-postgresql-interview-questions/' | relative_url }}">SQL and PostgreSQL interview questions</a></h3>
      <p>Useful if the role combines Spring Boot with database-heavy backend work.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/hibernate-jpa-interview-questions/' | relative_url }}">Hibernate and JPA interview questions</a></h3>
      <p>Useful when Spring discussions move into ORM behavior, entity lifecycle, and persistence tuning.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/rest-http-interview-questions/' | relative_url }}">REST and HTTP interview questions</a></h3>
      <p>Helpful when the target role focuses on Spring MVC controllers, API contracts, and endpoint design.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/java-concurrency-interview-questions/' | relative_url }}">Java concurrency interview questions</a></h3>
      <p>Useful when the role expects async execution, thread pools, or high-load services.</p>
    </article>
  </div>
</section>
