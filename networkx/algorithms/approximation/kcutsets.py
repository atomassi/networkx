"""Functions involving natural generalizations of the minimum cut problem."""

import networkx as nx
from networkx.utils import not_implemented_for

__all__ = ["minimum_multiway_cut", "minimum_k_cut"]


@not_implemented_for("directed")
@not_implemented_for("multigraph")
def minimum_multiway_cut(G, terminals, weight=None):
    """Compute an approximated Minimum Multiway Cut and the corresponding cut value.

    Given an undirected graph $G = (V, E)$ and a set of terminals
    $S = \{s_1, s_2, \dots ,s_k\} \subseteq V$, a multiway cut is a set of edges
    whose removal disconnects the terminals from each other.
    The min-multiway cut problem asks for the minimum weight multiway cut.
    The function computes a $(2-\\frac{2}{k})$-approximated Minimum Multiway Cut with $k$ being
    the number of terminals.

    Note that the case in which $k=2$ corresponds to the minimum $(s,t)$-cut and can
    be solved optimally in polynomial time. For $k \geq 3$, the problem is NP-hard [2]_.

    The function implements the algorithm described in [1]_. The algorithm is based on the concept
    of isolating cuts. An *isolating cut* for $s_i \in S$ is a set of edges whose removal disconnects
    $s_i$ from all $s_j \\in S$ with $j \\neq i$.

    The algorithm can be summarised as follows.

    1. For each $i=1, \dots, k$ compute a minimum weight isolating cut for $s_i$.
    2. Discard the heaviest of these cuts and output the union of the rest.

    Parameters
    ----------
    G : NetworkX graph
        Undirected graph.

    terminals : container of nodes
        A container with a subset of nodes of G.

    weight : string, optional (default = None)
        If None, every node has weight 1. If a string, use this node
        attribute as the node weight. A node without this attribute is
        assumed to have weight 1.

    Returns
    -------
    cut_value : scalar
        Value of the (approximated) minimum multiway cut.

    cutset : set
        Set of edges that, if removed from the graph, disconnects each
         terminal from all the others.

    Raises
    ------
    NetworkXNotImplemented
        If G is directed.

    References
    ----------
    .. [1]  Vazirani, Vijay V. *Approximation algorithms*.
            Springer Science & Business Media, 2013.
    .. [2]  Dahlhaus, Elias, et al. *The complexity of multiway cuts*.
            Proceedings of the twenty-fourth annual ACM symposium on Theory of computing. 1992
    """
    pass


@not_implemented_for("directed")
@not_implemented_for("multigraph")
def minimum_k_cut(G, k, weight=None):
    """Compute an approximated Minimum k-Cut and the corresponding cut value.

    Given an undirected graph $G = (V, E)$ and an integer $k \geq 2$, a $k$-cut is a
    set of edges whose removal leaves at least $k$ connected components.
    The Min-$k$-cut problem asks for a minimum weight $k$-cut.
    The function computes a $(2-\\frac{2}{k})$-approximated Minimum k-Cut.

    Note that the case in which $k=2$ corresponds to the global minimum cut and can
    be solved optimally in polynomial time. For $k \geq 3$, it's NP-hard [1]_.

    The function implements the algorithm described in [1]_.
    @TODO add description of the algorithm

    Parameters
    ----------
    G : NetworkX graph
        Undirected graph.

    k : integer
        The number of connected components the graph should have
        when the edges of the cut are removed.

    weight : string, optional (default = None)
        If None, every edge has weight 1. If a string, use this edge
        attribute as the edge weight. An edge without this attribute is
        assumed to have weight 1.

    Returns
    -------
    cut_value : scalar
        Value of the (approximated) minimum k-cut.

    cutset : set
        Set of edges whose removal leaves k connected components.

    Raises
    ------
    NetworkXNotImplemented
        If G is directed.

    See also
    --------
    networkx.algorithms.flow.minimum_cut

    References
    ----------
    .. [1]  Vazirani, Vijay V. *Approximation algorithms*.
            Springer Science & Business Media, 2013.
    """
    pass
