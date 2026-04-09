---
layout: default
title: Memory and Garbage Collection Interview Questions and Answers
description: Memory and garbage collection interview questions and answers about heap, stack, young and old generations, GC roots, leaks, pauses, and JVM memory behavior.
lang: en
image: /assets/social-preview/github-social-preview.png
---

<section class="hero">
  <span class="eyebrow">Topic Page</span>
  <h1>Memory and garbage collection interview questions and answers.</h1>
  <p class="lede">Memory and garbage collection questions are a classic part of Java interviews because they reveal whether a candidate understands what the JVM is doing underneath everyday code. This page collects the memory topics that are most useful in backend interviews and production troubleshooting conversations.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ '/questions/03-memory-and-garbage-collection/' | relative_url }}">Browse memory and garbage collection answers</a>
    <a class="button" href="{{ '/' | relative_url }}">Back to home</a>
  </div>
</section>

<section class="section">
  <h2>Why this topic matters in interviews</h2>
  <p>Interviewers ask memory questions because Java performance problems are often rooted in allocation patterns, object lifetime, reference reachability, and garbage collection behavior. Strong answers explain not only what the heap and stack are, but also how young and old generations differ, what makes an object eligible for collection, and why pauses or memory leaks happen in real systems.</p>
  <p>This topic also helps candidates explain broader runtime behavior. Once you understand how memory is managed, it becomes easier to reason about GC pressure, large object churn, cache design, and why seemingly harmless code can hurt latency under load.</p>
</section>

<section class="section">
  <h2>Representative memory and garbage collection interview questions</h2>
  <ol class="topic-list">
    <li>What is the difference between stack and heap memory?</li>
    <li>How does garbage collection work in Java?</li>
    <li>What are young and old generations?</li>
    <li>What are GC roots?</li>
    <li>When does an object become eligible for garbage collection?</li>
    <li>What is a memory leak in Java?</li>
    <li>What is the difference between minor and major GC?</li>
    <li>Why can stop-the-world pauses happen?</li>
    <li>How do strong, soft, weak, and phantom references differ?</li>
    <li>How would you investigate high memory usage or frequent GC pauses?</li>
  </ol>
</section>

<section class="section">
  <h2>Related pages</h2>
  <div class="card-grid">
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/java-collections-interview-questions/' | relative_url }}">Java collections interview questions</a></h3>
      <p>Useful because collection choice and object churn often have a direct effect on memory behavior.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/stream-api-interview-questions/' | relative_url }}">Stream API interview questions</a></h3>
      <p>Helpful when memory discussions touch on allocation patterns, temporary objects, and runtime overhead.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/java-concurrency-interview-questions/' | relative_url }}">Java concurrency interview questions</a></h3>
      <p>Natural companion when JVM behavior and throughput under load are discussed together.</p>
    </article>
  </div>
</section>
