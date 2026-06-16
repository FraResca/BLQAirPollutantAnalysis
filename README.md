# Forecasting and Interpreting Urban Air Pollution Under Weather, Traffic and Airport Influence

Last updated: `2026-05-17`

## 1. Purpose of the Repository

The objective of this repository is not only to obtain accurate predictive models, but also to understand **which type of information** makes pollutant concentrations predictable in an urban context influenced by:

- urban traffic measured by loop detectors;
- BLQ airport activity;
- meteorology;
- temporal memory in the pollutant time series;
- multi-station and multi-pollutant context.

The distinction between forecasting and interpretation is central. A model may predict a target accurately simply because it exploits the persistence of the series. This is operationally useful, but it is not sufficient to support a physical or source-specific interpretation. For this reason, the repository separates four analytical layers:

1. single-target forecasting with and without target autoregression;
2. multi-target forecasting to assess whether shared information exists across stations and pollutants;
3. `upwind/downwind` analysis and spatial gradients to test the physical consistency of airport-related signals;
4. an explicit `cross_pollutant` synthesis to compare chemical families and targets in a structured manner.

## 2. Current Repository Structure

The repository contains four distinct analytical components.

### 2.1. `explain` Component

Script:

- `explain_pollutants_by_feature_groups.py`

Purpose:

- multi-horizon single-target forecasting;
- model comparison;
- comparison between setups with and without target autoregression;
- targeted and extended ablations;
- group-level SHAP;
- native `XGBoost` feature importance;
- multioutput `XGBoost` comparison.

Main outputs:

- `Analysis/slurm_full_explain/advanced_temporal_cv_scores.csv`
- `Analysis/slurm_full_explain/advanced_temporal_cv_predictions.csv`
- `Analysis/slurm_full_explain/advanced_temporal_cv_summary.csv`
- `Analysis/slurm_full_explain/advanced_ablation_summary.csv`
- `Analysis/slurm_full_explain/advanced_extended_ablation_feature_sets.csv`
- `Analysis/slurm_full_explain/advanced_extended_ablation_scores.csv`
- `Analysis/slurm_full_explain/advanced_extended_ablation_summary.csv`
- `Analysis/slurm_full_explain/advanced_extended_ablation_fold_deltas.csv`
- `Analysis/slurm_full_explain/advanced_extended_ablation_delta_summary.csv`
- `Analysis/slurm_full_explain/advanced_group_shap.csv`
- `Analysis/slurm_full_explain/advanced_xgboost_native_feature_importances.csv`
- `Analysis/slurm_full_explain/advanced_xgboost_native_feature_importances_summary.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_xgboost_scores.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_xgboost_summary.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_ablation_summary.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_extended_ablation_feature_sets.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_extended_ablation_scores.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_extended_ablation_summary.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_extended_ablation_fold_deltas.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_extended_ablation_delta_summary.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_group_shap.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_xgboost_native_feature_importances.csv`
- `Analysis/slurm_full_explain/advanced_multioutput_xgboost_native_feature_importances_summary.csv`
- `Analysis/slurm_full_explain/advanced_runtime_profile.csv`
- `Analysis/slurm_full_explain/pollutant_station_reference_stats.csv`
- `Analysis/slurm_full_explain/plots/`

### 2.2. `upwind/downwind` Component

Script:

- `upwind_downwind_analysis.py`

Purpose:

- classification into `downwind`, `upwind`, `crosswind`, and `calm`;
- descriptive comparisons across wind regimes;
- regressions with `BLQ x downwind` interactions;
- `downwind/upwind` matching;
- block bootstrap;
- threshold sensitivity analysis;
- spatial gradients and multi-station DID analysis;
- SHAP by wind regime.

Main outputs:

- `Analysis/slurm_full_upwind/upwind_downwind_summary.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_blq_effects.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_distributed_lag_effects.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_regression_coefficients.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_distributed_lag_coefficients.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_matched_summary.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_matched_pairs.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_bootstrap_effects.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_threshold_sensitivity.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_classified_hours.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_blq_quantile_summary.csv`
- `Analysis/slurm_full_upwind/upwind_downwind_group_shap_by_regime.csv`
- `Analysis/slurm_full_upwind/multistation_did_summary.csv`
- `Analysis/slurm_full_upwind/multistation_did_regression_coefficients.csv`
- `Analysis/slurm_full_upwind/multistation_panel_long.csv`
- `Analysis/slurm_full_upwind/multistation_spatial_gradients.csv`
- `Analysis/slurm_full_upwind/multistation_spatial_gradient_summary.csv`
- `Analysis/slurm_full_upwind/multistation_station_wind_features.csv`
- `Analysis/slurm_full_upwind/plots/`

### 2.3. `airport_response` Component

Script:

- `airport_response_analysis.py`

Purpose:

- empirical target-versus-BLQ curves by regime;
- partial dependence profiles;
- event windows;
- exceedance probabilities;
- descriptive multi-station gradients.

Main outputs:

- `Analysis/airport_response_full/blq_empirical_response_curves.csv`
- `Analysis/airport_response_full/blq_partial_dependence_model_metrics.csv`
- `Analysis/airport_response_full/blq_partial_dependence_profiles.csv`
- `Analysis/airport_response_full/blq_event_windows_summary.csv`
- `Analysis/airport_response_full/blq_event_windows_long.csv`
- `Analysis/airport_response_full/blq_exceedance_probabilities.csv`
- `Analysis/airport_response_full/blq_spatial_gradient_response.csv`
- `Analysis/airport_response_full/plots/`

This component is **descriptive and explanatory**, not causal. Its purpose is to make the relationship among BLQ activity, wind, pollutant targets, and urban context more interpretable.

### 2.4. `cross_pollutant` Component

Script:

- `cross_pollutant_analysis.py`

Purpose:

- explicit comparison among targets and chemical families;
- synthesis of multi-horizon predictability;
- synthesis of dominant ablation groups;
- standardized synthesis of wind-regime contrasts.

Main outputs:

- `Analysis/cross_pollutant/cross_pollutant_predictability_summary.csv`
- `Analysis/cross_pollutant/cross_pollutant_predictability_target_overview.csv`
- `Analysis/cross_pollutant/cross_pollutant_predictability_pollutant_overview.csv`
- `Analysis/cross_pollutant/cross_pollutant_ablation_group_matrix.csv`
- `Analysis/cross_pollutant/cross_pollutant_ablation_top_groups.csv`
- `Analysis/cross_pollutant/cross_pollutant_targeted_ablation_summary.csv`
- `Analysis/cross_pollutant/cross_pollutant_group_shap_summary.csv`
- `Analysis/cross_pollutant/cross_pollutant_wind_response_summary.csv`
- `Analysis/cross_pollutant/cross_pollutant_wind_response_pollutant_overview.csv`
- `Analysis/cross_pollutant/cross_pollutant_overview.csv`
- `Analysis/cross_pollutant/cross_pollutant_family_overview.csv`
- `Analysis/cross_pollutant/cross_pollutant_runtime_profile.csv`
- `Analysis/cross_pollutant/plots/`

This fourth analysis does not refit the base models. It reorganizes and summarizes the results already produced by the other components.

## 3. Dataset

File:

- `Datasets_Raw/hourly_merged_2023_2025.csv`

Characteristics:

- `9,792` hourly rows
- `61` columns
- time span: `2024-05-29 00:00:00` -> `2025-07-10 23:00:00`
- temporal key: `datetime`

This file represents the common temporal intersection among all data blocks used in the analysis. This choice is methodologically appropriate because it avoids training models on periods in which one of the main information blocks is entirely unavailable.

### 3.1. Analysed Targets

The targets in the current run are:

- `NO2_porta_san_felice`
- `CO_porta_san_felice`
- `C6H6_porta_san_felice`
- `NO2_giardini_margherita`
- `NO2_via_chiarini`
- `O3_giardini_margherita`
- `O3_via_chiarini`

Descriptive statistics in the unified dataset:

| target                      | unit      |   minimum |       mean |     maximum |
| --------------------------- | --------- | --------: | ---------: | ----------: |
| `NO2_porta_san_felice`    | `ug/m3` | `2.000` | `26.586` |  `96.000` |
| `CO_porta_san_felice`     | `mg/m3` | `0.000` |  `0.468` |   `2.500` |
| `C6H6_porta_san_felice`   | `ug/m3` | `0.100` |  `0.961` |   `6.100` |
| `NO2_giardini_margherita` | `ug/m3` | `0.000` | `13.928` |  `63.000` |
| `NO2_via_chiarini`        | `ug/m3` | `0.000` | `15.560` |  `82.000` |
| `O3_giardini_margherita`  | `ug/m3` | `0.000` | `50.426` | `188.000` |
| `O3_via_chiarini`         | `ug/m3` | `0.000` | `45.810` | `213.000` |

Useful interpretation:

- `NO2` is available at three stations and is therefore the natural candidate for spatial comparisons;
- `O3` is available at the two external stations and is the most suitable target for studying meteorological and background dynamics;
- `CO` and `C6H6` are observed at Porta San Felice.

### 3.2. Information Blocks

The dataset integrates:

- BLQ airport traffic, including the `SERVICE_TYPE_CODE` decomposition;
- urban traffic from loop detectors, kept as separate columns;
- meteorology from two sources, `_aero` and `_centro`;
- other pollutants as multi-station and multi-pollutant context.

The loop-detector selection retains `20` unique sensors:

- `5` closest to BLQ;
- `5` closest to `Porta San Felice`;
- `5` closest to `Giardini Margherita`;
- `5` closest to `Via Chiarini`.

### 3.3. Temporal and Derived Features

The pipeline constructs:

- calendar features:
  - `hour`, `dayofweek`, `month`, `is_weekend`
  - `hour_sin`, `hour_cos`, `month_sin`, `month_cos`
- lags:
  - `_lag_1h`, `_lag_2h`, `_lag_3h`, `_lag_6h`, `_lag_12h`, `_lag_24h`
- differences:
  - `_diff_1h`
- rolling means:
  - `_rolling_3h_mean`, `_rolling_6h_mean`, `_rolling_12h_mean`, `_rolling_24h_mean`
- rolling standard deviations:
  - `_rolling_3h_std`, `_rolling_6h_std`, `_rolling_12h_std`, `_rolling_24h_std`
- wind interactions relative to the airport-to-station geometry.

This is technically important because the problem is not a static tabular regression task: the targets depend on lagged effects, recent accumulation, local variability, and transport regimes.

## 4. Running the Experiments

This README provides the information needed to set up the software environment, locate the input dataset, execute the analysis scripts, and inspect the generated outputs. The complete numerical outputs are stored in the CSV files listed below.

### 4.1. Environment Setup

The software environment is specified in:

- `environment.yml`

It defines a Python `3.11` conda environment with the packages required for data processing, forecasting, ablation, SHAP analysis, plotting, and output export.

To create the environment:

```bash
conda env create -f environment.yml
conda activate aira-local
```

If the environment already exists and needs to be updated:

```bash
conda env update -f environment.yml --prune
conda activate aira-local
```

### 4.2. Input Data

The recommended entry point for running the analyses is the merged hourly table:

- `Datasets_Raw/hourly_merged_2023_2025.csv`

The data-preparation scripts are relevant only if the original source files are available and the merged table must be rebuilt:

- `merge_blq_traffic.py`
- `merge_hourly_datasets.py`
- `merge_meteo.py`
- `merge_porta_san_felice_pollutants.py`
- `merge_spire_flow.py`

For ordinary experiment reproduction, start from `Datasets_Raw/hourly_merged_2023_2025.csv` and run the analysis scripts below.

### 4.3. Execution Order

The analyses should be run in this order:

1. `explain_pollutants_by_feature_groups.py`
2. `upwind_downwind_analysis.py`
3. `airport_response_analysis.py`
4. `cross_pollutant_analysis.py`

The order matters because `cross_pollutant_analysis.py` does not refit the base models. It reads and reorganizes CSV outputs produced by the forecasting and wind-regime analyses. Therefore, it must be executed after the upstream output files have been generated.

### 4.4. Local Commands

From the repository root, after activating the conda environment, run:

```bash
python explain_pollutants_by_feature_groups.py
python upwind_downwind_analysis.py
python airport_response_analysis.py
python cross_pollutant_analysis.py
```

For debugging or partial reproduction, run one component at a time and inspect its output directory before moving to the next script.

### 4.5. Expected Output Directories

The main generated outputs are written under `Analysis/`:

- `Analysis/slurm_full_explain/`
- `Analysis/slurm_full_upwind/`
- `Analysis/airport_response_full/`
- `Analysis/cross_pollutant/`

Each directory contains CSV files with metrics and summaries. Some directories also contain a `plots/` subdirectory.

### 4.6. Temporal Validation and Leakage Control

The forecasting code uses expanding-window temporal cross-validation. Each row is treated as a forecast origin: predictors at time `t` are used to predict the target at a later horizon `t+h`. Lagged and rolling features are shifted so that they only use information available at or before the forecast origin.

For each forecast horizon, training origins are restricted so that their labels occur before the first test origin. Missing predictor values are imputed inside each temporal fold using medians computed only on the training portion of that fold; the same medians are then applied to the corresponding test portion. These choices are used to prevent the model from seeing information from the future test period during training or preprocessing.

### 4.7. Cleaning and Rerunning

To reproduce a complete run from scratch, remove or archive the generated output directories under `Analysis/`, keep the input data under `Datasets_Raw/`, and run the analysis scripts again in the order described above.

Do not delete the input datasets unless the raw-data merge step is intentionally being repeated.

## 5. Location of the Complete Results

The complete result matrices, including all rows and all raw metrics, are stored in the CSV files generated under `Analysis/`.

To inspect **all results** without loss of detail:

- complete single-target metrics:
  - `Analysis/slurm_full_explain/advanced_temporal_cv_summary.csv`
- out-of-sample predictions:
  - `Analysis/slurm_full_explain/advanced_temporal_cv_predictions.csv`
- complete multioutput metrics:
  - `Analysis/slurm_full_explain/advanced_multioutput_xgboost_summary.csv`
- targeted ablations:
  - `Analysis/slurm_full_explain/advanced_ablation_summary.csv`
- extended single-target ablations:
  - `Analysis/slurm_full_explain/advanced_extended_ablation_delta_summary.csv`
- extended multioutput ablations:
  - `Analysis/slurm_full_explain/advanced_multioutput_extended_ablation_delta_summary.csv`
- SHAP and importance:
  - `Analysis/slurm_full_explain/advanced_group_shap.csv`
  - `Analysis/slurm_full_explain/advanced_multioutput_group_shap.csv`
  - `Analysis/slurm_full_explain/advanced_xgboost_native_feature_importances_summary.csv`
  - `Analysis/slurm_full_explain/advanced_multioutput_xgboost_native_feature_importances_summary.csv`
- `upwind/downwind` contrasts and regressions:
  - `Analysis/slurm_full_upwind/upwind_downwind_summary.csv`
  - `Analysis/slurm_full_upwind/upwind_downwind_blq_effects.csv`
  - `Analysis/slurm_full_upwind/upwind_downwind_matched_summary.csv`
  - `Analysis/slurm_full_upwind/upwind_downwind_bootstrap_effects.csv`
  - `Analysis/slurm_full_upwind/upwind_downwind_threshold_sensitivity.csv`
  - `Analysis/slurm_full_upwind/multistation_did_summary.csv`
- comparative syntheses:
  - `Analysis/cross_pollutant/cross_pollutant_overview.csv`
  - `Analysis/cross_pollutant/cross_pollutant_family_overview.csv`

The CSV outputs are the authoritative location for the complete quantitative results.
