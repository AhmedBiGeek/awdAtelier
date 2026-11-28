package com.awd.gateway;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

@RestController
public class HomeController {

    @GetMapping(value = "/", produces = MediaType.TEXT_HTML_VALUE)
    public Mono<String> home() {
        return Mono.just("""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                  <meta charset="UTF-8"/>
                  <title>API Gateway</title>
                  <style>
                    body { font-family: system-ui, sans-serif; max-width: 640px; margin: 3rem auto; padding: 0 1rem; }
                    a { display: block; margin: 0.4rem 0; }
                    code { background: #f2f2f2; padding: 0.1rem 0.35rem; }
                  </style>
                </head>
                <body>
                  <h1>API Gateway</h1>
                  <p>Port <code>8080</code> — use these routes:</p>
                  <a href="/api/candidates">/api/candidates</a>
                  <a href="/api/candidates/jobs">/api/candidates/jobs</a>
                  <a href="/api/jobs">/api/jobs</a>
                  <a href="/api/categories">/api/categories</a>
                  <a href="/actuator/health">/actuator/health</a>
                  <a href="http://localhost:8761">Eureka dashboard</a>
                </body>
                </html>
                """);
    }
}
