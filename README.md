# List of the strain weakening parameters for continental extension
## Table

AIF = Angle(s) of internal friction, Coh = cohesions, 

| Paper | Modified File | AIF | Coh | Str_Wk | End_Wk | Coh_F | Fric_F
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base | heron_2022.prm | 30 | 20.e6 | 0.5 | 1.5 | 0.5 | 0.5 |
| [Heron et al., 2019](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019TC005578) | heron_2019.prm | 20 | 20.e6 | 0. | 0.5 | 0.5 | 0.5 |
| [Gouiza & Naliboff, 2021](https://www.nature.com/articles/s41467-021-24945-5) | gouiza_2021_1.prm |


## List

- Base
  ```
  set Angles of internal friction = 30., 30., 30., 30., 30., 30., 0., 30.
  set Cohesions = 20.e6
  set Use strain weakening = true
  set Use plastic strain weakening = true
  set Start plasticity strain weakening intervals  = 0.5
  set End plasticity strain weakening intervals    = 1.5
  set Cohesion strain weakening factors            = 0.5
  set Friction strain weakening factors            = 0.5
  ```

- [Heron et al., 2019](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019TC005578)

  ```
  set Angles of internal friction = 20., 20., 20., 20., 20., 20., 0., 20.
  set Cohesions = 20.e6
  set Use strain weakening = true
  set Start strain weakening intervals  = 0.0
  set End strain weakening intervals    = 0.5
  set Cohesion strain weakening factors = 0.5
  set Friction strain weakening factors = 0.5
  ```