#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An enumerate function with extra features.
"""
import openturns as ot
import openturns.viewer as otv
import pylab as pl
from matplotlib.ticker import MaxNLocator


class SuperEnumerateFunction:
    def __init__(self, enumerate_function):
        """
        An enumerate function with extra features.

        Parameters
        ----------
        enumerateFunction : ot.EnumerateFunction()
            An enumerate function.

        Returns
        -------
        None.

        """
        self.enumerate_function = enumerate_function

    def draw_by_order(
        self,
        numberOfIndices,
        graphics_epsilon=0.1,
        figure_kw={"figsize": (4.0, 4.0)},
        legend_kw={"bbox_to_anchor": (1.0, 1.0), "loc": "upper left"},
    ):
        """
        Plots 2-dimensionnal multi-indices from an 2D enumerate function
        
        This prints the multi-indices up to the given numberOfIndices. 
        
        Parameters
        ----------
        numberOfIndices : int
            The number of multi-indices to plot.
        graphics_epsilon : float
            The graphical delta that we must add to that each multi-index
            do not overlap with the text.
        figure_kw : dict, optional
            The figure parameters. The default is {"figsize": (4.0, 4.0)}.
        legend_kw : dict, optional
            The legend parameters. The default is {"bbox_to_anchor":(1.0, 1.0), "loc":"upper left"}.
        
        Returns
        -------
        graph : ot.Graph()
            The plot.
        """
        # Add a delta to the text location, so that
        # it can be visually separated from the multi-index
        delta = ot.Point([graphics_epsilon] * 2)
        sample = ot.Sample(numberOfIndices, 2)
        sample_text = ot.Sample(numberOfIndices, 2)
        labellist = []
        for i in range(numberOfIndices):
            multiindice = self.enumerate_function(i)
            sample[i] = ot.Point(multiindice)
            sample_text[i] = ot.Point(multiindice) + delta
            labellist.append(str(i))
        # Create plot
        graph = ot.Graph("Multi-index set", "Indice 1", "Indice 2", True, "topright")
        cloud = ot.Cloud(sample)
        cloud.setPointStyle("circle")
        graph.add(cloud)
        text = ot.Text(sample_text, labellist)
        text.setTextSize(1.0)
        text.setColor("red")
        graph.add(text)
        view = otv.View(graph, figure_kw=figure_kw, legend_kw=legend_kw)
        pl.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        pl.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        _ = pl.axis("square")
        return view

    def multiindex_set_to_sample(self, index_collection):
        """
        Convert a list of indices into a sample of multi-indices

        Parameters
        ----------
        index_collection : list(int)
            The list of multi-index indices.

        Returns
        -------
        sample : ot.Sample(size, dimension)
            The sample of multi-indices.

        """
        multiindex_collection = []
        for i in index_collection:
            multiindex = self.enumerate_function(i)
            multiindex_collection.append(multiindex)
        # Gather multi-indices into a sample
        sample_size = len(multiindex_collection)
        dimension = self.enumerate_function.getDimension()
        sample = ot.Sample(sample_size, dimension)
        for i in range(sample_size):
            sample[i] = ot.Point(multiindex_collection[i])
        return sample

    def draw_by_layer(
        self,
        maximum_strata_index,
        figure_kw={"figsize": (4.0, 4.0)},
        legend_kw={"bbox_to_anchor": (1.0, 1.0), "loc": "upper left"},
    ):
        """
        Draw multi-indices by layer

        Parameters
        ----------
        maximum_strata_index : int
            The maximum strata index.
        figure_kw : dict, optional
            The figure parameters. The default is {"figsize": (4.0, 4.0)}.
        legend_kw : dict, optional
            The legend parameters. The default is {"bbox_to_anchor":(1.0, 1.0), "loc":"upper left"}.

        Returns
        -------
        view : ot.View()
            The graphics.

        """
        graph = ot.Graph("Linear enumeration rule", "$\\alpha_1$", "$\\alpha_2$", True)
        for strata_index in range(maximum_strata_index):
            strata_cardinal = self.enumerate_function.getStrataCardinal(strata_index)
            cumulated_cardinal = self.enumerate_function.getStrataCumulatedCardinal(
                strata_index
            )
            index_min = cumulated_cardinal - strata_cardinal
            index_collection = range(index_min, cumulated_cardinal)
            sample_in_layer = self.multiindex_set_to_sample(index_collection)
            cloud = ot.Cloud(sample_in_layer)
            cloud.setLegend("%d" % (strata_index))
            cloud.setPointStyle("circle")
            graph.add(cloud)
        palette = ot.DrawableImplementation.BuildDefaultPalette(maximum_strata_index)
        graph.setColors(palette)
        graph.setLegendPosition(("topright"))
        view = otv.View(graph, figure_kw=figure_kw, legend_kw=legend_kw)
        pl.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        pl.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        _ = pl.axis("square")
        return view
