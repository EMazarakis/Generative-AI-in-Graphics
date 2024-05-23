# Instructions for the relevant transformations

1.	Import .xlsx file with the human evaluation scores.
2.	We go Transform Data button --> Transform Data choice.
     - And we are into the power query editor.
4.	We choose the columns: Χρονική Σήμανση, Όνομα, Επώνυμο, Email.
5.	We go to Transform tab  Unpivot Columns  Unpivot Other Columns.
6.	2 new columns will be added:
a.	Attribute: this column contains the Questions
i.	We rename Attribute to Questions.
b.	Value: this column contains the scores for each question. (1 to 5)
i.	We rename Value to Evaluation Value.
7.	We go to Add Column tab Index Column  From 1.
a.	A new column with name Index added. 
8.	From the number in front of each question, we will create a column for the model’s name. (1-72:SD, 73-144:DL2,145-216:PA)
a.	We duplicate the column Questions. Right click and chose Duplicate Column.
b.	We go to the duplicated column and do split by the dot (.)
i.	Choose the duplicated column.
ii.	Right Click  Split Column  By Delimiter.
iii.	Chose Custom and add the dot (.).
iv.	Chose the option Left-most delimeter.
v.	2 new columns created: Questions – Copy 1 and Questions – Copy 2.
vi.	The column which contains only the number of the questions Questions – Copy 1, we renamed it to Question Number.
vii.	The second new column Questions – Copy 2, which contains only the questions we should remove it.
c.	Now we must create the column Model Name, which is a custom column.
i.	This column will be created with if-then-elseif with M language.
ii.	Question Range: 1-72=Stable Diffusion
iii.	Question Range: 73-144=DALL-E 2 
iv.	Question Range 145-216=Pix-Art-α
v.	We go to Add Column tab  Custom Column and add the M code.
1.	if [Question Number] >=1 and [Question Number] <=72 then "Stable Diffusion"
2.	else if [Question Number] >=73 and [Question Number] <=144 then "DALL-E 2"
3.	else if [Question Number] >=145 and [Question Number] <=216 then "Pix-Art-α"
4.	else "N/A"
vi.	We rename the custom column to Model Name
8.	From the number in front of each question, we will create a column for the task’s type (coloring, counting, conflicting, text, positional, faces)
a.	This column will be created with if-then-elseif with M language.
i.	Colouring: (1,12) or (73,84) or (145,156)
ii.	Counting: (13,24) or (85,96) or (157,168)
iii.	Conflicting: (25,36) or (97,108) or (169,180)
iv.	Text: (37,48) or (109,120) or (181,192)
v.	Positional: (49,60) or (121,132) or (193,204)
vi.	Faces: (61,72) or (133,144) or (205,216)
b.	We go to Add Column tab  Custom Column and add the M code.
i.	if ([Question Number] >=1 and [Question Number] <=12) or ([Question Number] >=73 and [Question Number] <=84) or ([Question Number] >=145 and [Question Number] <=156) then "Colouring"
ii.	else if ([Question Number] >=13 and [Question Number] <=24) or ([Question Number] >=85 and [Question Number] <=96) or ([Question Number] >=157 and [Question Number] <=168) then "Counting"
iii.	else if ([Question Number] >=25 and [Question Number] <=36) or ([Question Number] >=97 and [Question Number] <=108) or ([Question Number] >=169 and [Question Number] <=180) then "Conflicting"
iv.	else if ([Question Number] >=37 and [Question Number] <=48) or ([Question Number] >=109 and [Question Number] <=120) or ([Question Number] >=181 and [Question Number] <=192) then "Text"
v.	else if ([Question Number] >=49 and [Question Number] <=60) or ([Question Number] >=121 and [Question Number] <=132) or ([Question Number] >=193 and [Question Number] <=204) then "Positional"
vi.	else if ([Question Number] >=61 and [Question Number] <=72) or ([Question Number] >=133 and [Question Number] <=144) or ([Question Number] >=205 and [Question Number] <=216) then "Faces"
vii.	else "N/A"
c.	We rename the custom column to Task Type.
9.	Finally, we rename the query/table to 512_ratings.
10.	Now, we have to create some calculated columns:
a.	001.SumValues = SUM('512_ratings'[Evaluation Value])
b.	002.CountValues = COUNT('512_ratings'[Evaluation Value])
c.	003.Min Value = 1
d.	004.Max Value = 5
e.	005.Νumerator = ([001.SumValues] - [002.CountValues]*[003.Min Value])
f.	006.Denominator = ([004.Max Value]-[003.Min Value])*[002.CountValues]
g.	007.Norm = DIVIDE( [005.Νumerator],[006.Denominator],0)
h.	008.Norm% = [007.Norm]*100
i.	009.MaxNorm%ByModelTask = MAXX(ALL('512_ratings'[Model Name]),
CALCULATE([008.Norm%], ALLEXCEPT('512_ratings', '512_ratings'[Task Type], '512_ratings'[Model Name])))
j.	010.ColorMaxNorm% = IF([008.Norm%] < [009.MaxNorm%ByModelTask], "Black", "Red")

