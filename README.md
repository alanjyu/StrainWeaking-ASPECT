# List of strain weakening parameters for continental extension


## Table of parameters

- **AIF** = intial angle(s) of internal friction in deg
- **Coh** = intial cohesions in Pa
- **Str_Wk** = start plasticity strain weakening intervals
- **End_Wk** = end plasticity strain weakening intervals
- **Coh_F** = cohesion strain weakening factors
- **Fc_F** = friction strain weakening factors

| Source | Modified File | AIF | Coh | Str_Wk | End_Wk | Coh_F | Fc_F
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base | heron_2022.prm | 30 | 20.e6 | 0.5 | 1.5 | 0.5 | 0.5 |
| [Brune et al., 2013](https://www.sciencedirect.com/science/article/pii/S0040195113000899?via%3Dihub) | brune_2013.prm | 15 | 20.e6 | 0.05 | 1 | 0.5? | 0.5? |
| [Allken et al., 2012*](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2012GC004077) | allken_2012.prm | 15 | 20.e6 | 0.0 | 1.25 | 0.25? | 0.25? |
| [Duclaux et al., 2019*](https://www.sciencedirect.com/science/article/pii/S0012821X19306442) | | 15-2 | 20.e6-4.e6 | 0.5 | 1.5 | 0.1–0.5? | 0.1–0.5? |
| [Continental extension cookbook](https://github.com/geodynamics/aspect/blob/main/cookbooks/continental_extension/continental_extension.prm) | heron_2022_.25wf.prm| 30 | 20.e6 | 0.5 | 1.5 | 0.25 | 0.25
| [Heron et al., 2019](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019TC005578) | heron_2019.prm | 20 | 20.e6 | 0.0 | 0.5 | 0.5 | 0.5 |
| [Naliboff et al., 2020](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019GL086611) | | 30 | 20.e6 | 0.5 | 1.5 | 0.5 | 0.5 |
| [Gouiza & Naliboff, 2021](https://www.nature.com/articles/s41467-021-24945-5) | gouiza_2021.prm | 30 | 20.e6 | 0.5 | 1.5 | 1.0 | 0.25

\* These sources might use different equations or code libraries.


## List of original parameters

- [Naliboff et al., 2020](https://github.com/naliboff/aspect/blob/naliboff_etal_2020_grl/naliboff_etal_2020_grl.prm)

- [ASPECT continental extension cookbook](https://github.com/geodynamics/aspect/blob/main/cookbooks/continental_extension/continental_extension.prm)

- [Heron et al., 2019](https://github.com/heronphi/HeronTectonics2019/blob/master/HeronTectonics_M1.prm)

- [Gouiza & Naliboff, 2021](https://github.com/naliboff/aspect/tree/labrador_sea_gouiza_naliboff_2020/labrador_sea_gouiza_naliboff_2020_models).