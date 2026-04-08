---
layout: default
title: SQL and PostgreSQL Interview Questions and Answers
description: SQL and PostgreSQL interview questions and answers about indexes, JOINs, GROUP BY, HAVING, window functions, MVCC, VACUUM, ANALYZE, and query optimization.
lang: en
image: /assets/social-preview/github-social-preview.png
---

<section class="hero">
  <span class="eyebrow">Topic Page</span>
  <h1>SQL and PostgreSQL interview questions and answers.</h1>
  <p class="lede">Backend Java roles almost always touch SQL, and PostgreSQL questions show up often because they expose how well a candidate understands data access, performance, and transactional behavior. This page groups the most important interview themes from that area.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ site.github.repository_url }}/blob/master/README.md#1-databases--sql--postgresql">Browse SQL and PostgreSQL section on GitHub</a>
    <a class="button" href="{{ '/' | relative_url }}">Back to home</a>
  </div>
</section>

<section class="section">
  <h2>What good answers look like</h2>
  <p>Strong SQL interview answers balance clarity and trade-offs. You should be able to explain what an index is, but also when indexes hurt write performance. You should know what a JOIN does, but also when a correlated subquery or window function may be a better fit. PostgreSQL-specific questions often go further into MVCC, VACUUM, and planner behavior because these are common sources of real production issues.</p>
  <p>This topic cluster is especially valuable for Java backend interviews that combine Spring Boot with Hibernate, JPA, or direct SQL optimization work.</p>
</section>

<section class="section">
  <h2>Representative SQL and PostgreSQL interview questions</h2>
  <ol class="topic-list">
    <li>What are indexes and why are they needed?</li>
    <li>How does a B-tree index work?</li>
    <li>What is a composite index?</li>
    <li>What is the difference between <code>INNER JOIN</code> and <code>LEFT JOIN</code>?</li>
    <li>What is a correlated subquery?</li>
    <li>What is the difference between <code>WHERE</code> and <code>HAVING</code>?</li>
    <li>What do window functions do?</li>
    <li>How does MVCC work in PostgreSQL?</li>
    <li>What is <code>VACUUM</code> in PostgreSQL?</li>
    <li>How do you optimize a slow query?</li>
  </ol>
</section>

<section class="section">
  <h2>Related pages</h2>
  <div class="card-grid">
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/spring-boot-interview-questions/' | relative_url }}">Spring Boot interview questions</a></h3>
      <p>Useful because most Spring roles eventually connect ORM abstractions back to SQL behavior.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ site.github.repository_url }}/blob/master/README.md#16-hibernate--jpa">Hibernate and JPA questions on GitHub</a></h3>
      <p>A strong next step when moving from query foundations to ORM internals and persistence design.</p>
    </article>
  </div>
</section>
