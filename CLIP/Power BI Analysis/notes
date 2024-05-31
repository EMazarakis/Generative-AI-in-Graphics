This folder contains the pbix file and the relevant source file (003.clip_metrics_file_ViT_L_14@336px.xlsx) of the power bi.

On the power bi file we do some transformations.

We go to the model tab, to the Mean% and Median% columns and do the decimal places 3.
We also summarize the Size column by: None.

Then we make some new columns:
1. Model Name = SWITCH('clip_metrics_file_ViT_L_14@336p'[Model],"SD", "Stable Diffusion", "DL", "DALL-E 2", "PA", "Pix-Art-α")

2. MaxMeanPercent = 
VAR MaxTaskMeanPercent =
    MAXX(
        ALL('clip_metrics_file_ViT_L_14@336p'[Model Name]),
        CALCULATE(
            MAX('clip_metrics_file_ViT_L_14@336p'[Mean%]),
            ALLEXCEPT('clip_metrics_file_ViT_L_14@336p', 'clip_metrics_file_ViT_L_14@336p'[Task], 'clip_metrics_file_ViT_L_14@336p'[Size])
        )
    )
RETURN
    MaxTaskMeanPercent  //For each category, across model names and size we find the Max value of Mean %

3. ColorMaxMeanPercent = IF('clip_metrics_file_ViT_L_14@336p'[Mean%] < 'clip_metrics_file_ViT_L_14@336p'[MaxMeanPercent], "Black", "Red")
//If the Mean% is less than the MaxMeanPercent return the color Black, otherwise Red. That means that the max value it will have red color.

4. MaxMedianPercent = 
VAR MaxTaskMedianPercent =
    MAXX(
        ALL('clip_metrics_file_ViT_L_14@336p'[Model Name]),
        CALCULATE(
            MAX('clip_metrics_file_ViT_L_14@336p'[Median%]),
            ALLEXCEPT('clip_metrics_file_ViT_L_14@336p', 'clip_metrics_file_ViT_L_14@336p'[Task], 'clip_metrics_file_ViT_L_14@336p'[Size])
        )
    )
RETURN
    MaxTaskMedianPercent //For each category, across model names and size we find the Max value of Median %


5. ColorMaxMedianPercent = IF('clip_metrics_file_ViT_L_14@336p'[Median%] < 'clip_metrics_file_ViT_L_14@336p'[MaxMedianPercent], "Black", "Red")
//If the Median% is less than the MaxMedianPercent return the color Black, otherwise Red. That means that the max value it will have red color.


To do the conditional formatiing in opder to highlight the max value of each clustred column, we go to column chart: 
Visual --> Data Labels --> Value --> Choose conditional formating and do the following:
Rules --> choose the column ColorMaxMeanPercent, and if the value is Red return the Red colour.
