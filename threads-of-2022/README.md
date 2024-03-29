# Threads of 2022: A Year of Checkouts

Welcome to the first installment of the Fibery Library! Using data from 2022, our team of knitters and crocheters on the library staff crafted scarves which visualize the number of loaned physical items per day. We chose different color palettes to represent different user groups. With each scarf, you can "read" the color changes from left to right, where each row represents one day of checkouts, from January through December. The darker the color, the more checkouts there were on that row's corresponding day. Try to spot patterns such as the beginnings and ends of academic terms, days of the week, and big campus weekends!

["Threads of 2022: a Year of Checkouts"](www.dartgo.org/fibery-library) is currently on display on Berry Main Street through March 2024.

Special thanks goes out to the core team of project organizers: Samara Cary, Simon Stone, Stephen Krueger, Tara Custer, and Daniel Lin. Additional thanks to the Library Innovation Fund for providing support to purchase materials for this project! Physical exhibit designed by Dennis Grady. Digital exhibit designed by Daniel Lin.


## How to use this repository
This repository contains the data and code to reproduce the data visualizations (heatmaps) that were used to create the knitting/crocheting patterns. It has the following structure:

- `data/`: Contains the raw data extracted from out internal database
- `notebooks/`: Contains a [Jupyter notebook ](https://docs.jupyter.org/en/latest/index.html) that produces the heatmaps
- `out/`: The output folder for the files produced by the code
- `ppt/`: A PowerPoint slide deck that was used at the project's kickoff event
- `res/`: Handouts created for the project's crafters, and a file containing the mapping of yarn color names to hex codes


## Getting started

1. Install the project requirements:

```
pip install -r requirements.txt
```

2. Run the notebook `notebooks/library-collection.ipynb`
3. Find the output in `out/`.


## Licensing
<table >
<tbody>
  <tr>
    <td style="padding:0px;border-width:0px;vertical-align:center">
    Created by Simon Stone for Dartmouth College Library under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons CC BY-NC 4.0 License</a>.<br>For questions, comments, or improvements, email <a href="mailto:researchdatahelp@groups.dartmouth.edu">Research Data Services</a>.
    </td>
    <td style="padding:0 0 0 1em;border-width:0px;vertical-align:center"><img alt="Creative Commons License" src="https://i.creativecommons.org/l/by/4.0/88x31.png"/></td>
  </tr>
</tbody>
</table>