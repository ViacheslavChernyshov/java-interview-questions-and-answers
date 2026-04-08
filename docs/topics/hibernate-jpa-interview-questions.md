---
layout: default
title: Hibernate and JPA Interview Questions and Answers
description: Hibernate and JPA interview questions and answers about entity states, lazy loading, N+1 queries, dirty checking, flush, cascade, and optimistic locking.
lang: en
image: /assets/social-preview/github-social-preview.png
---

<section class="hero">
  <span class="eyebrow">Topic Page</span>
  <h1>Hibernate and JPA interview questions and answers.</h1>
  <p class="lede">Hibernate and JPA questions appear in many Java backend interviews because they reveal whether a candidate understands what really happens between Java objects, SQL, transactions, and persistence context behavior. This page pulls together the ORM topics that usually matter most.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ site.github.repository_url }}/blob/master/README.md#16-hibernate--jpa">Browse Hibernate and JPA section on GitHub</a>
    <a class="button" href="{{ '/' | relative_url }}">Back to home</a>
  </div>
</section>

<section class="section">
  <h2>What interviewers usually look for here</h2>
  <p>Strong Hibernate answers go beyond annotations. Interviewers often want to know whether you understand the persistence context, entity states, lazy loading, dirty checking, flushing, and how those mechanics translate into SQL queries and production bugs. This is also where candidates are often tested on trade-offs: convenience versus control, abstraction versus performance, and default behavior versus explicit tuning.</p>
  <p>If you can explain why N+1 happens, when cascade settings are dangerous, and how optimistic locking protects concurrent updates, you usually sound much stronger than candidates who only know the API surface.</p>
</section>

<section class="section">
  <h2>Representative Hibernate and JPA interview questions</h2>
  <ol class="topic-list">
    <li>What is JPA and how does Hibernate relate to it?</li>
    <li>What entity states exist in Hibernate?</li>
    <li>What is the persistence context?</li>
    <li>What is dirty checking and how does it work?</li>
    <li>What is the difference between <code>persist</code>, <code>merge</code>, and <code>save</code>?</li>
    <li>What is lazy loading and when does it cause problems?</li>
    <li>What is the N+1 query problem?</li>
    <li>What do cascade types do and when can they be dangerous?</li>
    <li>What is the difference between optimistic and pessimistic locking?</li>
    <li>When does Hibernate flush SQL to the database?</li>
  </ol>
</section>

<section class="section">
  <h2>Related pages</h2>
  <div class="card-grid">
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/sql-postgresql-interview-questions/' | relative_url }}">SQL and PostgreSQL interview questions</a></h3>
      <p>Best next step if you want to connect ORM abstractions back to real query behavior and database performance.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/spring-boot-interview-questions/' | relative_url }}">Spring Boot interview questions</a></h3>
      <p>Useful because most Java backend roles combine Spring data access patterns with Hibernate mechanics.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/rest-http-interview-questions/' | relative_url }}">REST and HTTP interview questions</a></h3>
      <p>Helpful when the role expects full-stack backend reasoning from controller layer down to persistence.</p>
    </article>
  </div>
</section>
