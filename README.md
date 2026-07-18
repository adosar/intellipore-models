## About
Fine-tuned model checkpoints from the paper *IntelliPore: A Foundation Model for Gas Adsorption in Porous Materials*.

The checkpoints can be used either for inference or as initialization for further fine-tuning on related adsorption tasks.

**1. Install AIdsorb**

```bash
pip install "aidsorb>=3.0.0"
```

<details>
<summary><strong>2. Load one of the available checkpoints</strong> (click to expand)</summary>

```python
  {
    "CO\u2082 uptake at 298 K and 2.5 bar (MOFs)": {
        "model_id": "hmof_CO2-298-2.5",
        "units": "[mol/kg]"
    },
    "CH\u2084 uptake at 298 K and 2.5 bar (MOFs)": {
        "model_id": "hmof_CH4-298-2.5",
        "units": "[mol/kg]"
    },
    "N\u2082 uptake at 298 K and 0.9 bar (MOFs)": {
        "model_id": "hmof_N2-298-0.9",
        "units": "[mol/kg]"
    },
    "Xe binary uptake at 273 K and 10 bar (MOFs)": {
        "model_id": "hmof_Xe-273-10",
        "units": "[mol/kg]"
    },
    "Kr binary uptake at 273 K and 10 bar (MOFs)": {
        "model_id": "hmof_Kr-273-10",
        "units": "[mol/kg]"
    },
    "H\u2082 uptake at 77 K and 2 bar (MOFs)": {
        "model_id": "hmof_H2-77-2",
        "units": "[g/L]"
    },
    "CO\u2082 heat of adsorption at 298 K and 2.5 bar (MOFs)": {
        "model_id": "hmofheat_CO2-298K-2.5bar",
        "units": "[kJ/mol]"
    },
    "H\u2082 heat of adsorption at 77 K and 2 bar (MOFs)": {
        "model_id": "hmofheat_H2-77K-2bar",
        "units": "[kJ/mol]"
    },
    "CH\u2084 uptake at 298 K and 5.8 bar (COFs)": {
        "model_id": "cof_lowbar",
        "units": "[v STP/v]"
    },
    "CH\u2084 uptake at 298 K and 65 bar (COFs)": {
        "model_id": "cof_highbar",
        "units": "[v STP/v]"
    },
    "CH\u2084 uptake at 298 K and 1 bar (PPNs)": {
        "model_id": "ppn_1bar",
        "units": "[cm3 STP/cm3]"
    },
    "CH\u2084 uptake at 298 K and 65 bar (PPNs)": {
        "model_id": "ppn_65bar",
        "units": "[cm3 STP/cm3]"
    },
    "CH\u2084 unitless Henry coefficient at 298 K (ZEOs)": {
        "model_id": "zeolite_unitless_KH",
        "units": "[unitless]"
    },
    "CH\u2084 isosteric heat of adsorption at 298 K (ZEOs)": {
        "model_id": "zeolite_heat_of_adsorption",
        "units": "[kJ/mol]"
    },
    "C\u2083H\u2088/C\u2083H\u2086 selectivity at 298 K and 1 bar (MOFs)": {
        "model_id": "c3h6c3h8coremof_C3H8_C3H6_Selectivity_1bar",
        "units": "[unitless]"
    },
    "C\u2083H\u2088/C\u2083H\u2086 infinite dillution selectivity at 298 K (MOFs)": {
        "model_id": "c3h6c3h8coremof_C3H8_C3H6_Selectivity_infinite",
        "units": "[unitless]"
    },
    "C\u2083H\u2086 binary uptake at 298 K and 1 bar (MOFs)": {
        "model_id": "c3h6c3h8coremof_C3H6_loadings",
        "units": "[mol/kg]"
    },
    "C\u2083H\u2088 binary uptake at 298 K and 1 bar (MOFs)": {
        "model_id": "c3h6c3h8coremof_C3H8_loadings",
        "units": "[mol/kg]"
    },
    "C₃H₈ binary uptake × selectivity (C₃H₈/C₃H₆) at 298 K and 1 bar (MOFs)": {
        "model_id": "c3h6c3h8coremof_TSN_S_1Bar",
        "units": "[unitless]"
    },
    "C\u2083H\u2088 log Henry coefficient at 298 K (MOFs)": {
        "model_id": "c3h6c3h8coremof_C3H8_Henry_298K",
        "units": "[log(mol/kg/Pa)]"
    },
    "C\u2083H\u2086 log Henry coefficient at 298 K (MOFs)": {
        "model_id": "c3h6c3h8coremof_C3H6_Henry_298K",
        "units": "[log(mol/kg/Pa)]"
    },
    "CH\u2084/N\u2082 selectivity and 298 K and 0.1 bar (MOFs)": {
        "model_id": "ch4n2_ch4n2ratio-0.1bar",
        "units": "[unitless]"
    },
    "CH\u2084/N\u2082 selectivity and 298 K and 10 bar (MOFs)": {
        "model_id": "ch4n2_ch4n2ratio-10bar",
        "units": "[unitless]"
    },
    "CH\u2084/N\u2082 selectivity and 298 K and 1 bar (MOFs)": {
        "model_id": "ch4n2_ch4n2ratio-1bar",
        "units": "[unitless]"
    },
    "CH\u2084 binary uptake at 298 K and 0.1 bar (MOFs)": {
        "model_id": "ch4n2_ch4uptake-0.1bar",
        "units": "[mol/kg]"
    },
    "CH\u2084 binary uptake at 298 K and 10 bar (MOFs)": {
        "model_id": "ch4n2_ch4uptake-10bar",
        "units": "[mol/kg]"
    },
    "CH\u2084 binary uptake at 298 K and 1 bar (MOFs)": {
        "model_id": "ch4n2_ch4uptake-1bar",
        "units": "[mol/kg]"
    },
    "N\u2082 binary uptake at 298 K and 0.1 bar (MOFs)": {
        "model_id": "ch4n2_n2uptake-0.1bar",
        "units": "[mol/kg]"
    },
    "N\u2082 binary uptake at 298 K and 10 bar (MOFs)": {
        "model_id": "ch4n2_n2uptake-10bar",
        "units": "[mol/kg]"
    },
    "N\u2082 binary uptake at 298 K and 1 bar (MOFs)": {
        "model_id": "ch4n2_n2uptake-1bar",
        "units": "[mol/kg]"
    }
}
```
</details>



```python
import torch
from aidsorb.modules.voxels import IntelliPore

model_id = ...

url = 'https://raw.githubusercontent.com/adosar/intellipore-models/master/finetuned_models/{model_id}.ckpt'
state_dict = torch.hub.load_state_dict_from_url(url, map_location='cpu')

model = IntelliPore()
model.load_state_dict(state_dict)

# Your code goes here
```

For examples of inference and fine-tuning, please refer to the [**AIdsorb Gallery**](https://aidsorb.readthedocs.io/en/stable/auto_examples/index.html).

## Performance summary
Comparison of IntelliPore and other baseline models for gas adsorption prediction in terms of $R^2$ (higher is better). 

**Best** model is highlighted with **bold**.

| Adsorption Property                                                                 | CGCNN   | MOFormer   | PMTransformer   | SpbNet    | IntelliPore |
|:------------------------------------------------------------------------------------|:--------|:-----------|:----------------|:----------|:--------------|
| CO₂ uptake at 298 K and 2.5 bar (MOFs)                                              | 0.605   | 0.563      | 0.886           | **0.944** | 0.943         |
| CH₄ uptake at 298 K and 2.5 bar (MOFs)                                              | 0.667   | 0.608      | 0.853           | 0.924     | **0.960**     |
| N₂ uptake at 298 K and 0.9 bar (MOFs)                                               | 0.634   | 0.562      | 0.777           | 0.874     | **0.906**     |
| Xe binary uptake at 273 K and 10 bar (MOFs)                                         | 0.697   | 0.675      | 0.901           | 0.926     | **0.946**     |
| Kr binary uptake at 273 K and 10 bar (MOFs)                                         | 0.733   | 0.736      | 0.842           | 0.856     | **0.899**     |
| H₂ uptake at 77 K and 2 bar (MOFs)                                                  | 0.621   | 0.627      | 0.932           | 0.975     | **0.985**     |
| CO₂ heat of adsorption at 298 K and 2.5 bar (MOFs)                                  | 0.812   | 0.755      | 0.906           | 0.903     | **0.909**     |
| H₂ heat of adsorption at 77 K and 2 bar (MOFs)                                      | 0.798   | 0.711      | 0.895           | 0.905     | **0.926**     |
| CH₄ uptake at 298 K and 5.8 bar (COFs)                                              | 0.516   | 0.566      | 0.909           | 0.952     | **0.989**     |
| CH₄ uptake at 298 K and 65 bar (COFs)                                               | 0.556   | 0.541      | 0.967           | 0.976     | **0.987**     |
| CH₄ uptake at 298 K and 1 bar (PPNs)                                                | 0.293   | 0.417      | 0.559           | 0.890     | **0.973**     |
| CH₄ uptake at 298 K and 65 bar (PPNs)                                               | 0.692   | 0.636      | 0.942           | 0.968     | **0.987**     |
| CH₄ unitless Henry coefficient at 298 K (ZEOs)                                      | 0.237   | 0.107      | 0.435           | 0.809     | **0.910**     |
| CH₄ isosteric heat of adsorption at 298 K (ZEOs)                                    | 0.411   | 0.388      | 0.836           | 0.935     | **0.973**     |
| C₃H₈/C₃H₆ selectivity at 298 K and 1 bar (MOFs)                                     | 0.020   | -0.010     | 0.401           | 0.317     | **0.742**     |
| C₃H₈/C₃H₆ infinite dillution selectivity at 298 K (MOFs)                            | 0.293   | 0.201      | 0.599           | 0.627     | **0.916**     |
| C₃H₆ binary uptake at 298 K and 1 bar (MOFs)                                        | 0.727   | 0.602      | 0.824           | 0.900     | **0.942**     |
| C₃H₈ binary uptake at 298 K and 1 bar (MOFs)                                        | 0.736   | 0.689      | 0.875           | 0.923     | **0.946**     |
| $N_\mathrm{C_3H_8} \times \log(S_\mathrm{C_3H_8/C_3H_6})$ at 298 K and 1 bar (MOFs) | 0.358   | 0.266      | 0.528           | 0.630     | **0.816**     |
| C₃H₈ log Henry coefficient at 298 K (MOFs)                                          | 0.239   | 0.064      | 0.337           | 0.351     | **0.873**     |
| C₃H₆ log Henry coefficient at 298 K (MOFs)                                          | 0.299   | 0.192      | 0.481           | 0.647     | **0.898**     |
| CH₄/N₂ selectivity and 298 K and 0.1 bar (MOFs)                                     | 0.752   | 0.286      | 0.823           | 0.866     | **0.885**     |
| CH₄/N₂ selectivity and 298 K and 10 bar (MOFs)                                      | 0.728   | 0.723      | 0.912           | 0.947     | **0.962**     |
| CH₄/N₂ selectivity and 298 K and 1 bar (MOFs)                                       | 0.718   | 0.698      | 0.905           | 0.949     | **0.968**     |
| CH₄ binary uptake at 298 K and 0.1 bar (MOFs)                                       | 0.523   | 0.452      | 0.714           | 0.900     | **0.951**     |
| CH₄ binary uptake at 298 K and 10 bar (MOFs)                                        | 0.701   | 0.707      | 0.815           | 0.929     | **0.935**     |
| CH₄ binary uptake at 298 K and 1 bar (MOFs)                                         | 0.496   | 0.617      | 0.769           | 0.918     | **0.951**     |
| N₂ binary uptake at 298 K and 0.1 bar (MOFs)                                        | 0.550   | 0.588      | 0.710           | 0.869     | **0.911**     |
| N₂ binary uptake at 298 K and 10 bar (MOFs)                                         | 0.792   | 0.814      | 0.886           | **0.943** | **0.943**     |
| N₂ binary uptake at 298 K and 1 bar (MOFs)                                          | 0.617   | 0.661      | 0.783           | **0.924** | 0.905         |



## Citing

If you use any of these models in your research, please cite:

```bibtex
@article{intellipore2025,
  title   = {IntelliPore: A Foundation Model for Gas Adsorption in Porous Materials},
  author  = {Author, A. and Author, B. and ...},
  journal = {Journal},
  year    = {2025},
  doi     = {TBD}
}
```
