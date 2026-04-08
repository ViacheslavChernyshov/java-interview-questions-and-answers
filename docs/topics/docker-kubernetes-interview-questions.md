---
layout: default
title: Docker and Kubernetes Interview Questions and Answers
description: Docker and Kubernetes interview questions and answers about images, containers, layers, networking, volumes, deployments, probes, config, and scaling.
lang: en
image: /assets/social-preview/github-social-preview.png
---

<section class="hero">
  <span class="eyebrow">Topic Page</span>
  <h1>Docker and Kubernetes interview questions and answers.</h1>
  <p class="lede">Docker and Kubernetes questions appear when backend roles include delivery, platform awareness, or cloud-native operations. This page focuses on the container and orchestration concepts that are most useful for Java engineers preparing for modern production-focused interviews.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ site.github.repository_url }}/blob/master/README.md#14-docker--kubernetes">Browse Docker and Kubernetes section on GitHub</a>
    <a class="button" href="{{ '/' | relative_url }}">Back to home</a>
  </div>
</section>

<section class="section">
  <h2>What interviewers tend to probe here</h2>
  <p>These questions usually test whether you understand the difference between packaging an application and operating it reliably. Good answers explain how images are built, how containers behave at runtime, how configuration is injected, and how Kubernetes manages rollout, health checks, scaling, and recovery.</p>
  <p>You do not need to sound like a platform engineer for every Java role, but it helps a lot if you can explain how your service gets from code to a running, observable, restartable production workload.</p>
</section>

<section class="section">
  <h2>Representative Docker and Kubernetes interview questions</h2>
  <ol class="topic-list">
    <li>What is the difference between an image and a container?</li>
    <li>How do Docker layers work and why do they matter?</li>
    <li>What is the role of a <code>Dockerfile</code>?</li>
    <li>How are environment variables, volumes, and networks used in containers?</li>
    <li>What is the difference between a Kubernetes Pod and a Deployment?</li>
    <li>What do liveness and readiness probes do?</li>
    <li>How do ConfigMaps and Secrets differ?</li>
    <li>What is horizontal scaling in Kubernetes?</li>
    <li>How do rolling updates work?</li>
    <li>What problems usually appear when Java services run in containers?</li>
  </ol>
</section>

<section class="section">
  <h2>Related pages</h2>
  <div class="card-grid">
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/kafka-interview-questions/' | relative_url }}">Kafka interview questions</a></h3>
      <p>Useful when distributed services, event consumers, and platform operations are discussed together.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/spring-boot-interview-questions/' | relative_url }}">Spring Boot interview questions</a></h3>
      <p>Helpful because container questions often connect directly to how Spring services boot and expose health endpoints.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/java-concurrency-interview-questions/' | relative_url }}">Java concurrency interview questions</a></h3>
      <p>Useful when containerized services run background jobs, schedulers, or high-load async workloads.</p>
    </article>
  </div>
</section>
