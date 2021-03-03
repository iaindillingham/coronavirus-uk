# Coronavirus in the UK

Charts of data from the [Coronavirus in the UK][] API.
You can read about them in [this thread][1] on Twitter.
Despite the statistics making grim reading, some people said some nice things about the charts.

The *specs/\*.vg.json* [Vega][] specs describe the charts.
Paste each into the [Vega Editor][]'s *Vega* tab.
To add style, paste *specs/config.json* into the *Config* tab.
(You will need to have [Avenir Next Condensed][] installed to see the charts as I designed them.)

The *src/print_url.py* Python script prints a URL for querying the Coronavirus in the UK API.
It doesn't have any dependencies: run `python3 src/print_url.py` to print the URL.

## Notebooks

To execute the notebooks in the *notebooks* directory, first install [Poetry][].
Then, execute `poetry install`.
Finally, execute `poetry run jupyter lab`.

[1]: https://twitter.com/iaindillingham/status/1357256652974661632
[Avenir Next Condensed]: https://www.fonts.com/font/linotype/avenir-next/condensed
[Coronavirus in the UK]: https://coronavirus.data.gov.uk/
[Poetry]: https://python-poetry.org/
[Vega Editor]: https://vega.github.io/editor/#/custom/vega
[Vega]: https://vega.github.io/vega/
