# List of strain weakening parameters for continental extension


## Table of parameters

- **AIF** = intial angle(s) of internal friction
- **Coh** = intial cohesions
- **Str_Wk** = start plasticity strain weakening intervals
- **End_Wk** = end plasticity strain weakening intervals
- **Coh_F** = cohesion strain weakening factors
- **Fc_F** = friction strain weakening factors

| Source | Modified File | AIF | Coh | Str_Wk | End_Wk | Coh_F | Fc_F
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base | heron_2022.prm | 30 | 20.e6 | 0.5 | 1.5 | 0.5 | 0.5 |
| [Allken et al., 2013*](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2012GC004077) | | 15 | 20.e6 | 0.0 | 1.25 | 0.25? | 0.25? |
| [Continental extension cookbook](https://github.com/geodynamics/aspect/blob/main/cookbooks/continental_extension/continental_extension.prm) | | 30 | 20.e6 | 0.5 | 1.5 | 0.25 | 0.25
| [Heron et al., 2019](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019TC005578) | heron_2019.prm | 20 | 20.e6 | 0.0 | 0.5 | 0.5 | 0.5 |
| [Naliboff et al., 2020](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019GL086611) | heron_2022.prm | 30 | 20.e6 | 0.5 | 1.5 | 0.5 | 0.5 |
| [Gouiza & Naliboff, 2021](https://www.nature.com/articles/s41467-021-24945-5) | gouiza_2021.prm | 30 | 20.e6 | 0.5 | 1.5 | 1.0 | 0.25

\* These sources might use different equations or code libraries.


## List of modified codeblocks

The following codeblocks have been modified to be compatible with the base parameter file.

- Base & Naliboff et al., 2020 [(original file)](https://github.com/naliboff/aspect/blob/naliboff_etal_2020_grl/naliboff_etal_2020_grl.prm)
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

- Continental extension cookbook [(original file)](https://github.com/geodynamics/aspect/blob/main/cookbooks/continental_extension/continental_extension.prm)

  ```
  # Plasticity parameters
  set Angles of internal friction = 30., 30., 30., 30., 30., 30., 0., 30.
  set Cohesions = 20.e6

  set Strain weakening mechanism = plastic weakening with plastic strain only
  set Start plasticity strain weakening intervals  = 0.5
  set End plasticity strain weakening intervals    = 1.5
  set Cohesion strain weakening factors            = 0.25
  set Friction strain weakening factors            = 0.25
  ```

- Heron et al., 2019 [(original file)](https://github.com/heronphi/HeronTectonics2019/blob/master/HeronTectonics_M1.prm)

  ```
  set Angles of internal friction = 20., 20., 20., 20., 20., 20., 0., 20.
  set Cohesions = 20.e6

  set Use strain weakening = true
  set Start strain weakening intervals  = 0.0
  set End strain weakening intervals    = 0.5
  set Cohesion strain weakening factors = 0.5
  set Friction strain weakening factors = 0.5
  ```

- Gouiza & Naliboff, 2021 [(original files)](https://github.com/naliboff/aspect/tree/labrador_sea_gouiza_naliboff_2020/labrador_sea_gouiza_naliboff_2020_models). Note that the models also considered viscous strain. This will be incorporated into the modified file later.

  ```
  set Angles of internal friction = 30., 30., 30., 30., 30., 30., 0., 30.
  set Cohesions = 20.e6

  set Use strain weakening                        = true
  set Use viscous strain weakening                = true
  set Start prefactor strain weakening intervals  = 0.5 
  set End prefactor strain weakening intervals    = 1.5 
  set Prefactor strain weakening factors          = 0.25 
  set Use plastic strain weakening                = true
  set Start plasticity strain weakening intervals = 0.5
  set End plasticity strain weakening intervals   = 1.5
  set Cohesion strain weakening factors           = 1.0
  set Friction strain weakening factors           = 0.25
  ```

## To read
  
- [Huismans & Beaumont, 2003](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2002JB002026)
- [Duclaux et al., 2019](https://www.sciencedirect.com/science/article/pii/S0012821X19306442) 