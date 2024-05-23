# Instructions for the relevant transformations

1.	Import .xlsx file with the human evaluation scores.
2.	We go Transform Data button --> Transform Data choice.
     - And we are into the power query editor.
3.	We choose the columns: Χρονική Σήμανση, Όνομα, Επώνυμο, Email.
4.	We go to Transform tab --> Unpivot Columns --> Unpivot Other Columns.
5.	2 new columns will be added:
     - Attribute: this column contains the Questions
          - We rename Attribute to Questions.
     - Value: this column contains the scores for each question. (1 to 5)
          - We rename Value to Evaluation Value.
6.	We go to Add Column tab --> Index Column --> From 1.
     - A new column with name Index added. 
7.	From the number in front of each question, we will create a column for the model’s name. (1-72:SD, 73-144:DL2,145-216:PA)
     - We duplicate the column Questions. Right click and chose Duplicate Column.
     - We go to the duplicated column and do split by the dot (.)
          - Choose the duplicated column.
          - Right Click  Split Column  By Delimiter.
          - Chose Custom and add the dot (.).
          - Chose the option Left-most delimeter.
          - 2 new columns created: Questions – Copy 1 and Questions – Copy 2.
          - The column which contains only the number of the questions Questions – Copy 1, we renamed it to Question Number.
          - The second new column Questions – Copy 2, which contains only the questions we should remove it.
     - Now we must create the column Model Name, which is a custom column.
          - This column will be created with if-then-elseif with M language.
          - Question Range: 1-72=Stable Diffusion
          - Question Range: 73-144=DALL-E 2 
          - Question Range 145-216=Pix-Art-α
          - We go to Add Column tab --> Custom Column and add the M code.
               if [Question Number] >=1 and [Question Number] <=72 then "Stable Diffusion"
	          else if [Question Number] >=73 and [Question Number] <=144 then "DALL-E 2"
	          else if [Question Number] >=145 and [Question Number] <=216 then "Pix-Art-α"
	          else "N/A"
          - We rename the custom column to Model Name
8.	From the number in front of each question, we will create a column for the task’s type (coloring, counting, conflicting, text, positional, faces)
     - This column will be created with if-then-elseif with M language.
          - Colouring: (1,12) or (73,84) or (145,156)
          - Counting: (13,24) or (85,96) or (157,168)
          - Conflicting: (25,36) or (97,108) or (169,180)
          - Text: (37,48) or (109,120) or (181,192)
          - Positional: (49,60) or (121,132) or (193,204)
          - Faces: (61,72) or (133,144) or (205,216)
     - We go to Add Column tab  Custom Column and add the M code.
            if ([Question Number] >=1 and [Question Number] <=12) or ([Question Number] >=73 and [Question Number] <=84) or ([Question Number] >=145 and [Question Number] <=156) then "Colouring"
            else if ([Question Number] >=13 and [Question Number] <=24) or ([Question Number] >=85 and [Question Number] <=96) or ([Question Number] >=157 and [Question Number] <=168) then "Counting"
            else if ([Question Number] >=25 and [Question Number] <=36) or ([Question Number] >=97 and [Question Number] <=108) or ([Question Number] >=169 and [Question Number] <=180) then "Conflicting"
          else if ([Question Number] >=37 and [Question Number] <=48) or ([Question Number] >=109 and [Question Number] <=120) or ([Question Number] >=181 and [Question Number] <=192) then "Text"
          else if ([Question Number] >=49 and [Question Number] <=60) or ([Question Number] >=121 and [Question Number] <=132) or ([Question Number] >=193 and [Question Number] <=204) then "Positional"
          else if ([Question Number] >=61 and [Question Number] <=72) or ([Question Number] >=133 and [Question Number] <=144) or ([Question Number] >=205 and [Question Number] <=216) then "Faces"
          else "N/A"
     - We rename the custom column to Task Type.
9.	Finally, we rename the query/table to 512_ratings.
10.	Now, we have to create some calculated columns:
     - 001.SumValues = SUM('512_ratings'[Evaluation Value])
     - 002.CountValues = COUNT('512_ratings'[Evaluation Value])
     - 003.Min Value = 1
     - 004.Max Value = 5
     - 005.Νumerator = ([001.SumValues] - [002.CountValues]*[003.Min Value])
     - 006.Denominator = ([004.Max Value]-[003.Min Value])*[002.CountValues]
     - 007.Norm = DIVIDE( [005.Νumerator],[006.Denominator],0)
     - 008.Norm% = [007.Norm]*100
     - 009.MaxNorm%ByModelTask = MAXX(ALL('512_ratings'[Model Name]),CALCULATE([008.Norm%], ALLEXCEPT('512_ratings', '512_ratings'[Task Type], '512_ratings'[Model Name])))
     - 010.ColorMaxNorm% = IF([008.Norm%] < [009.MaxNorm%ByModelTask], "Black", "Red")
