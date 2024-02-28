Flowchart for URDF Workflow
```mermaid
flowchart LR
    A(Joint State Publisher GUI)
    B(Joint State)
    C(Simulated Actuator)
    D(Real Actuator)
    E(Robot State Publisher)
    F(URDF)
    G(/tf_static)
    H(/tf)
    I(/robot_description)

    A --> B
    C --> B
    D --> B
    B --> E
    F --> E
    E --> G
    E --> H
    E --> I
```
