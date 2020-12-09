
```mermaid
graph TD;
    S((Start)) --> A[authenticate]
    A -->|ok| C[input commandline to access cloud]
    C -->|next command| C
    C --> E((END))
```