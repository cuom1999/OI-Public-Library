# Translation Quality Audit

This audit is separate from `MANIFEST.md`. The manifest tracks whether a source
document has a Vietnamese LaTeX file; it does not prove that the file is a full
translation.

For annual national training-team collections, `QUALITY_WORKLIST.md` expands
this audit into an article-by-article queue generated from the translated
tables of contents.

## High-Confidence Undertranslated Files

No annual national training-team collection is currently known to be
article-incomplete.

## Spot-Checked Repaired Articles

These non-annual files were flagged by the line/page audit and then repaired
or reclassified.

| Translation | Source pages | Resolution |
| --- | ---: | --- |
| `sources/ioi/2009-wu-sen-binary-thinking.tex` | 29 | Expanded from the A4 article source: restored the binary preface, detailed Matrix proof, Sudoku search discussion, Requirements sign-mask proof, Cow XOR trie details, and fuller appendix statements. |
| `sources/ioi/2009-jia-zhihao-sg-game-variants.tex` | 24 | Restored the article front matter: preface, reading advice, stated article features, and acknowledgments. The technical SG-game body had already been translated. |
| `sources/ioi/2009-cao-qinxiang-k-dynamic-subtraction-games.tex` | 44 | Expanded compressed passages from the A4 article: contest significance of game theory, CEOI 2008 knight pattern/strategy intuition, and the BOI 2008 Game official-solution critique, counterexample, and optimized interval-state argument. |
| `sources/ioi/2009-tang-keyin-expectation-problems.tex` | 17 | Repaired after source comparison: restored the omitted Highlander derangement notes, fixed the RedIsGood recurrence, and added the linear-system caveat about non-unique systems and reachable variables. The file covers all five examples from the A4 article. |

## Low-Density Files Reviewed And Kept As Translated

These files still look short by line/page ratio, but source inspection showed
that the low density is explained by slide formatting or sparse source text.
They remain `translated`.

| Translation | Source pages | Evidence |
| --- | ---: | --- |
| `sources/data-structure/power-of-statistics-segment-tree-zhang-kunwei.tex` | 102 | Source is an Impress slide deck. The Vietnamese file follows the slide sequence from range sums and heap layout through lazy tags, order statistics, dynamic segment trees, balanced trees, and the practice problem; decorative/interlude slides and figures are folded into prose. |
| `sources/data-structure/persistent-data-structures-chen-lijie.tex` | 23 | Source is a LaTeX-produced A4 note whose text extraction is mojibake. The translation follows the source ToC through persistent segment trees, block lists, kth-number queries, tree-path queries, offline-to-online conversion, persistent Treap, editor example, dynamic convex hull, Almost, and acknowledgments. |
| `sources/mathematics/simple-mathematical-logic-li-kaiwei.tex` | 40 | Source is an Impress slide deck. The translation covers propositional logic, equivalence laws, normal forms, SAT/2-SAT, DPLL, SMT, bit-vector examples, applications, and references. |
| `sources/others/functional-programming-guo-jiabao.tex` | 54 | Source is a PowerPoint slide deck. The translation follows the lecture from halting problem and lambda calculus through recursion, fixed points, Haskell basics, lazy evaluation, higher-order functions, and mainstream language features. |
| `sources/mathematics/inclusion-exclusion-zhang-kunlong.tex` | 39 | Source is a PowerPoint-style lecture deck. The translation covers the union/intersection formulas, Sylvester formula, restricted permutations, sieve applications, Euler phi, derangements, rook polynomials, generalized inclusion--exclusion, Stirling numbers, non-adjacent combinations, and couple-seating example. |
| `sources/usaco/usaco-monthly-contest-solutions.tex` | 21 | Source is a compact A4 table handout. The translation preserves all 29 contest blocks from USACO 2002 February through USACO 2008 January and uses a dense `solutiontable` structure, explaining the low line/page ratio. |
| `sources/ioi/2001-gao-hanrui-round-table-data-structures.tex` | 12 | Source is a sparse A4 export with repeated slide/article content. The translation covers the round-table statement, sequential and linked simulations, segmented combined structure, timing table, extensions, and conclusion. |
| `sources/ioi/2001/li-yuan-enumerating-directed-trees.tex` | 21 | Source is an Impress slide deck. The translation reconstructs the tree-order and transformation diagrams in TikZ and covers the enumeration algorithm, deletion/recomposition cases, complexity, and application note. |
| `sources/ioi/2001-li-yiming-computational-geometry.tex` | 12 | Source is a short A4 speech draft with Pascal appendices. The article body is translated, and the three raw programs are represented as Vietnamese algorithm explanations under the project's code-template exception. |
| `sources/ioi/2001/zhang-yifei-high-precision-factorial.tex` | 24 | Source is an Impress slide deck. The translation covers the high-precision overview, Pascal type limits, `Comp` storage, binary representation, multiplication optimization, prime factorization, binary exponentiation, improved squaring, and closing summary. |
| `sources/ioi/2002/wang-zhikun-search-order-selection.tex` | 22 | Source is an Impress slide deck with one blank final page. The translation covers every nonblank slide: interval arrangement, search-order principles, operator decoding, static/dynamic ordering, Prime Square, Basketball Championship, pruning, Birthday Cake, and conclusion. |
| `sources/ioi/2002/luo-ji-game-problem-two-methods.tex` | 41 | Source is an Impress slide deck. The translation reconstructs the slide diagrams/proofs in prose and covers the full arc: stone-taking, general method, limitations, special method, Fibonacci proof, comparison, and conclusion. |
| `sources/ioi/2002/yang-minmin-construction-method.tex` | 32 | Source is an Impress slide deck. The translation mirrors the slide topics: construction-method traits, direct construction, crane and interval-coloring examples, case construction, board traversal, induction construction, scheduling examples, and conclusion. |
| `sources/ioi/2002/zhang-jialin-fast-polynomial-multiplication.tex` | 29 | Source is an Impress slide deck. The translation covers polynomial representation, point-value multiplication, interpolation, lemmas and proofs, recursive transform, inverse transform, algorithm flow, iterative improvement, and experimental comparison. |
| `sources/ioi/2002/huang-yun-dancing-flies-isomorphism.tex` | 20 | Source is a sparse LibreOffice Impress slide export. The translation follows the slide sequence, recreates the opening problem/example diagrams in TikZ, and expands the graph-isomorphism abstraction, functional-graph structure, canonical representations, algorithm, complexity, and conclusion into article prose. |
| `sources/ioi/2002/sun-linchun-parity-optimization.tex` | 18 | Source is an Impress slide deck. The translation covers the Parity statement, common processing framework, algorithms 1--4, prefix-parity transformation, equivalence classes, `same`/`opp`, DSU/hash implementation, runtime comparison table, and conclusion; visual interval diagrams are folded into prose/tables. |
| `sources/ioi/2002/li-pengxu-half-plane-intersection.tex` | 30 | Source combines a short A4 paper with sparse slide-extract pages. The translation covers the paper sections and adds an appendix for the slide-text portion, including half-plane intersection variants, convex polygon intersection, Hotter and Colder, Milk/Nice Milk, Video, Triathlon, Run away, Voronoi, and references. |
| `sources/ioi/2002/he-jiangzhou-gaussian-elimination-linear-equations.tex` | 22 | Source is an Impress slide deck. The translation follows the full slide sequence: GPA ranking model, general augmented-matrix form, worked elimination example, elimination/back-substitution formulas, pivot selection and precision example, no-solution and infinite-solution cases, complexity/error analysis, exact integer elimination, gear-ratio application, and conclusion. |
| `sources/ioi/2002/he-lin-conjecture-applications.tex` | 40 | Source bundles a 14-page article and a slide deck. The translation covers the article's abstract, analogy sections, examples 1--4 with statements/input/output/analysis, induction theory, conclusion, references, and a condensed translated appendix for the slide deck; slide-only layouts and figures are folded into prose. |
| `sources/ioi/2002/li-rui-binary-method-statistics.tex` | 63 | Source is a bundled A4 paper plus slide extract. The translation covers the article's segment tree, static dynamic-statistics method, binary-search-tree statistics, virtual binary tree, KOP example, longest monotone subsequence optimization, conclusion, references, and a separate appendix translating the slide text. |
| `sources/ioi/2002/zhou-wenchao-tree-structures-programming.tex` | 22 | Source is an Impress slide deck. The translation covers the substantive slides on union-find list/tree forms, direct find, path compression, segment tree definition/update/measure/line count, BIT construction/update/prefix sum, two-dimensional extension, and conclusion; visuals are reconstructed as prose, ASCII, and pseudocode. |
| `sources/ioi/2002/yu-wei-ulam-game-coding.tex` | 16 | Source is an Impress slide deck. The translation covers the Ulam game, no-error binary search, filtering by error classes, operation example, question-count estimate, coding method, error-correcting/parity code construction, XOR-to-question mapping, count comparison, and extensions, with slide diagrams reconstructed in TikZ/tables. |
| `sources/ioi/2002/zhang-yifei-combinatorial-games.tex` | 35 | Source is a bundled A4 article plus slide extract. The translation covers the game definitions, simplification and xor analogy, proof, Game B extension, Game C mex construction, Stripes application note, algorithmic/philosophical summary, and an appendix translating the slide text. |
| `sources/ioi/2004/wu-jingyue-minimum-spanning-tree-applications.tex` | 29 | Source is a Word/pdfFactory article plus long Pascal appendices. The translation covers the MST definitions, safe-edge theorem/proof, Kruskal, Prim, Maintain, Robot, Arctic Network, conclusion, acknowledgments, and references; full code listings are represented as pseudocode under the code-template exception. |
| `sources/ioi/2004/zhu-chenguang-egg-dropping-dp-optimization.tex` | 43 | Source PDF page 1--22 is Zhu Chenguang's article; pages 23--43 are unrelated bundled papers. The translation covers the relevant article, Ural statement, five algorithms, summary, conclusion, references, and related code listings; figures 1--3 are represented by textual/array schematics where needed. |
| `sources/ioi/2004/zhu-zeyuan-multiple-string-matching.tex` | 66 | Source PDF is a bundled export: pages 1--23 are Zhu Zeyuan's multiple-string-matching article and are translated here; the remaining pages duplicate the Zhu Chenguang egg-dropping article, which is also tracked as `IOI中国国家候选队论文/2004/朱晨光.pdf` and translated separately. |
| `sources/ioi/2009-qi-zichao-tree-path-divide-conquer.tex` | 29 | Source is a text-extractable tagged PDF. The translation covers all major sections, theorem proofs, examples 1--5, path decomposition, further discussion, references, thanks, and URL appendix; original explanatory figures are described in text rather than reproduced. |
| `sources/ioi/2009-jiang-biye-spfa-optimization-applications.tex` | 37 | Source is an Acrobat PDFMaker article. The translation covers SPFA basics, DFS/BFS optimizations, benchmark tables, Johnson, positive-cycle detection, state pruning, difference constraints, DP applications, iterative equation solving, Apple game DP, appendix problem statements, source-file list, references, and acknowledgments. |
| `sources/ioi/2009-luo-keqiang-low-level-optimization.tex` | 37 | Source is a born-digital Word-generated PDF. The translation covers the full paper structure: platform setup, introductory optimization example, instruction efficiency, arithmetic optimization, cache and branch behavior, out-of-order execution, bit tricks, multidimensional arrays, applications, tables, experiments, conclusion, references, and acknowledgments. |
| `sources/ioi/2008-xiao-hanjun-depth-and-breadth-analysis.tex` | 23 | Source is a LaTeX/DVIPDFMx PDF. The translation covers the abstract, keywords, four chapters, all four examples and problem statements, references, and acknowledgments; original figures are simplified into prose, tables, or schematics. |
| `sources/ioi/2008-yu-linyun-sequence-problems-reduction.tex` | 35 | Source is a LaTeX/DVIPDFMx PDF. The translation covers the abstract, preface, all chapters, all four examples and problem statements, algorithms, sample and constraint tables, references, and acknowledgments; two explanatory Count figures are omitted but the surrounding technical text is present. |
| `sources/ioi/2007-he-sen-data-organization.tex` | 15 | Source is a text-extractable PDF. The translation covers the abstract, data-form and operation-order framework, Jinming budget variants, tree fruit counting, flight-route planning with reverse-time bridge maintenance, conclusion, references, acknowledgments, and translated appendix problem statements. |
| `sources/ioi/2007-matroid-introduction-liu-yuchen.tex` | 15 | Source is a text-extractable Writer PDF. The translation covers the matroid definitions, greedy optimization proof, scheduling application, linear/uniform/dual/matching examples, Shannon switching game extension, conclusion, references, Russell-paradox appendix, and DSU scheduling appendix. |
| `sources/ioi/2009-li-jiyang-segment-skip-list.tex` | 16 | Source is a WPS Office article. The translation covers skip-list basics, segment skip-list extraction, formal SSL definition, DP/segment information maintenance, insertion/deletion proofs, expected time and space analysis, parameter discussion, comparison against segment and balanced trees, and references; figures are represented by explicit descriptions rather than bare captions. |
| `sources/ioi/2009-gao-yihan-digit-counting.tex` | 13 | Source is a text-extractable Word-generated PDF. The translation covers the abstract, introduction, all three digit-counting examples, conclusion, acknowledgments, reference, appendix URLs, and the example-3 dependency diagram as a Vietnamese table; one final direct-enumeration code block is summarized under the code-template exception. |
| `sources/ioi/2007-yang-mu-divide-and-combine-thinking.tex` | 17 | Source is a text-extractable LibreOffice PDF. The translation covers the abstract, introduction, all three examples, conclusion, acknowledgments, references, and both appendix problem statements with samples; cover, blank, and standalone ToC pages are omitted. |
| `sources/ioi/2004/zhou-yuan-numeric-geometric-thinking.tex` | 21 | Source PDF bundles Zhou Yuan's 12-page numeric/geometric-thinking article followed by an unrelated Splay Tree article. The translation covers the full Zhou Yuan article, Sequence appendix, attachment note, and references; main figures are reconstructed in TikZ, and the unrelated appended paper is tracked separately. |
| `sources/ioi/2004/xue-mao-dynamic-statistics-segment-tree-rectangle-cutting.tex` | 31 | Source is a text-extractable pdfFactory article with appendices. The translation follows the source ToC, all sections and subsections, references, five appendices, reconstructed Pascal algorithm listings, and the War problem statement; figures are converted into prose, formulas, arrays, or algorithm descriptions. |
| `sources/ioi/2004/xiao-tian-layered-graph-thinking.tex` | 19 | Source is a Word/doc-derived pdfFactory PDF. The translation covers the layered-graph article, references, and the non-code appendix problem statement; main diagrams are recreated in TikZ, while long appendix programs are summarized under the code-template exception. |
| `sources/ioi/2002/sun-fangcheng-bipartite-graph-algorithms.tex` | 34 | Source is a text-extractable PDF containing a paper plus slide/presentation section. The translation covers matching, bipartite recognition, maximum matching, minimum cover, best matching/KM, conclusion, Hall theorem appendix, references, and the slide text; visual slide elements are simplified. |
| `sources/ioi/2000/jiang-peng-constructive-method-models.tex` | 26 | Source is a text-extractable PDF with appendices and Pascal listings. The translation covers the construction-method article, all six problem discussions, modeling sections, hotel network-flow model, conclusion, references, and selected appendix problem statements; long code appendices are summarized under the code-template exception. |
| `sources/ioi/2000-guo-yi-mathematical-models.tex` | 11 | Source is an A4 Writer article. The translation covers model reliability/solvability, the IOI 1993 travel-route models, Catalan examples, 01-string and Black-and-White graph modeling, conclusion, and references; the two Pascal appendices are represented as algorithm descriptions under the code-template exception. |

## Article-Coverage Complete Annual Collections

These annual collections now have a translated section for every ToC article.
They may still need proofreading of formulas, OCR-heavy passages, and diagrams,
but they should not be counted as ToC-only or partially covered collections.

| Translation | Source pages | Current state | Notes |
| --- | ---: | --- | --- |
| `sources/ioi/2013-national-training-team-collection.tex` | 137 | ToC plus all twelve articles translated | Final inclusion--exclusion article translated from physical PDF pages 125--137. |
| `sources/ioi/2014-national-training-team-collection.tex` | 228 | ToC plus all fifteen articles translated | Final best-\(k\)-solution article translated from physical PDF pages 199--228. |
| `sources/ioi/2015-national-training-team-collection.tex` | 291 | ToC plus all fifteen articles translated | Final set-power article translated from physical PDF pages 275--291. |
| `sources/ioi/2016-national-training-team-collection.tex` | 234 | ToC plus all fifteen articles translated | Final \emph{move} report translated from physical PDF pages 225--234. |
| `sources/ioi/2017-national-training-team-collection.tex` | 204 | ToC plus all fifteen articles translated | Final genome-reconstruction report translated from physical PDF pages 192--204. |
| `sources/ioi/2018-national-training-team-collection.tex` | 210 | ToC plus all fifteen articles translated | Final Euler graph generation/counting article translated from physical PDF pages 194--210. |
| `sources/ioi/2019-national-training-team-collection.tex` | 231 | ToC plus all fifteen articles translated | Final Young tableau article translated after filtering watermark/header noise. |
| `sources/ioi/2024-national-training-team-collection.tex` | 424 | ToC plus all twenty-five articles translated | Final minimum-ratio-cycle article translated from physical PDF pages 408--422; back/contact pages 423--424 are not article body. |
| `sources/ioi/2025-national-training-team-collection.tex` | 168 | ToC plus all twenty-three articles translated | Final linear-congruence-inequality article translated from physical PDF pages 161--168. |
| `sources/ioi/2020-national-training-team-collection.tex` | 196 | ToC plus all fourteen articles translated | Proofread mathematical notation and examples when polishing. |
| `sources/ioi/2022-national-training-team-collection.tex` | 246 | ToC plus all fourteen articles translated | OCR-backed collection; proofread formulas, pseudocode, and diagram descriptions. |
| `sources/ioi/2023-national-training-team-collection.tex` | 249 | ToC plus all eighteen articles translated | Final convexity-optimization article translated from physical PDF pages 234--249. |

## Large Reference PDFs That Are Only Notes

These are not IOI team reports, but they also should not be counted as full
book translations. The manifest marks these rows as `reference-note`, so they
do not inflate the count of full translated documents.

| Translation | Source pages | Current state | Recommendation |
| --- | ---: | --- | --- |
| `sources/english/introduction-to-algorithms-3e-clrs.tex` | 1313 | Book metadata and chapter-structure note | Keep as `reference-note` unless selected licensed chapters are translated explicitly. |
| `sources/english/computer-systems-programmers-perspective-3e.tex` | 1120 | Book metadata and chapter-structure note | Keep as `reference-note` unless selected licensed chapters are translated explicitly. |
| `sources/english/concrete-mathematics-graham-knuth-patashnik.tex` | 670 | Book metadata and chapter-structure note | Keep as `reference-note`; translate selected math background excerpts only when scope and rights are clear. |
| `sources/english/a-probability-path-resnick.tex` | 459 | Book metadata and chapter-structure note | Keep as `reference-note`; translate selected probability excerpts only when scope and rights are clear. |
| `sources/english/data-structures-network-algorithms-tarjan.tex` | 142 | ToC/preface-focused note | Keep as `reference-note`; it remains the shortest candidate if selected licensed chapters are later requested. |
| `sources/usaco/usaco-ten-year-problem-anthology-v10.tex` | 266 | Preface and recovered index only | Keep as `reference-note`; needs OCR or replacement source text before any detailed problem translation. |
| `sources/others/not-so-short-introduction-to-latex.tex` | 107 | Adapted Vietnamese guide, not a full manual translation | Keep as `reference-note`; source front matter, full index, figures, and many detailed manual passages are intentionally not reproduced. |

## Lower-Confidence Compression Suspects

These files were flagged by low line-per-page ratios. The current rows below
have been reviewed as slide-deck companion notes rather than full article/book
translations. The manifest marks them as `companion-note`, so they do not
inflate the full translated-document count.

| Translation | Source pages | Notes |
| --- | ---: | --- |
| `sources/ioi/2000-luo-ji-mathematical-modeling.tex` | 16 | Reviewed as an A4 Writer paper. The Vietnamese covers the main article body, all named examples, statistical table, model-selection discussion, and summary, but compresses the appendix beyond code listings: explanatory appendix notes, full 01-string statement details, and the complete bibliography are not fully translated. |
| `sources/ioi/1999/chen-hong-picture-data-structures.tex` | 15 | Reviewed as a text-extractable LibreOffice article. The Vietnamese covers the prose and code-level ideas for Picture, elementary and super-elementary segments, linear scan, segment-tree sweep, comparison, extension, conclusion, and references, but omits the geometric figures; later labeled states such as `[G,A]`, `[E,C]`, `[H,F]`, `[D,B]`, and scan line `L` rely on missing diagrams. |
| `sources/ioi/2002/sorting-networks-fu-wenjie.tex` | 8 | Reviewed as a text-extractable LibreOffice article. The Vietnamese covers definitions, the 0-1 principle, half-cleaner proof, bitonic sorter, merger, recursive sorter, complexity, and summary, but omits comparator-network diagrams whose topology is substantive, including the half-cleaner cases and the detailed \(n=8\) sorting network. |
| `sources/ioi/2004/ge-rong-special-enumeration-thinking.tex` | 27 | Reviewed as a Word/pdfFactory article. The Vietnamese covers the main 9-page paper, but source pages 9--27 contain long standalone problem statements and Pascal program appendices for Smart Typist, Logic Island, Strawberry, and threshold matching; the translation replaces most of that appendix material with compact notes and pseudocode. |
| `sources/ioi/2006-zhu-zeyuan-half-plane-intersection.tex` | 11 | Reviewed as a bilingual Word/PDFMaker article. The translation covers the prose on half-plane and convex-polygon intersection, divide and conquer, S&I steps, practical value, linear-sort note, and bibliography, but does not reproduce figures i--vii, including algorithmic CPI sweep, polar-angle, stack/deque, and zero-intersection diagrams. |
| `sources/ioi/2007-wang-xinshang-layered-network-flow.tex` | 26 | Reviewed as a text-extractable PDF. The translation covers MPLA, Dinic, MPM, complexity analysis, two Dinic applications, benchmark tables, references, and thanks, but omits original diagrams and heavily summarizes appendix problem statements, including much of the I/O, sample, scoring, and data wording. |
| `sources/ioi/2007-hu-botao-minimum-cut-model-applications.tex` | 45 | Reviewed as a Word/PDFMaker article. The translation covers most main prose on minimum-cut models, maximum weight closure, density subgraph, bipartite cover/independent set, examples, summary, acknowledgments, references, and appendix headings, but misses many substantive figures, condenses the How to Solve It appendix and glossary, and has at least one source-attribution mismatch in the problem table. |
| `sources/ioi/2007-qiu-rongqi-euler-circuit-applications.tex` | 26 | Reviewed as a Writer article. The translation covers the main Euler theory article and examples, but omits figures 1--6 and reduces non-code appendices 3--5: the source has full English problem statements for Play on Words, Depot Rearrangement, and Gambling, while Vietnamese currently gives short summaries and samples. |
| `sources/ioi/2009-dong-huaxing-trie-applications.tex` | 21 | Reviewed as a text-extractable PDF. The translation covers trie basics, search, sorting, DP transition pruning, LCP/LCA, extensions, limits, references, thanks, and appendix problems, but drops full input/output-format wording from several main examples and replaces multiple figures with ASCII/text summaries. |
| `sources/ioi/2009-luo-suiqian-suffix-array.tex` | 25 | Reviewed as a WPS Office article. The translation covers definitions, doubling, DC3, comparison table/experiment, LCP, all 13 application examples, references, and acknowledgments, but omits figures 1--8, including explanatory diagrams for SA/rank, doubling, DC3, LCP/RMQ, grouping, palindrome transform, repeated substrings, and LCS. |
| `sources/ioi/2009-zhou-erjin-estimation-functions.tex` | 19 | Reviewed as an A4 Writer paper. The translation covers the main ideas and all named examples, but heavily condenses the table of contents, experiment tables, generated-node counts, Sokoban boards, runtime graph, Largest Fence illustration, TSP MST illustration, and comparison charts. |
| `sources/ioi/2009-zhang-kunwei-mathematical-induction.tex` | 22 | Reviewed as Word-style A4 article. The translation follows the outline and all examples, but condenses the long introduction, detailed derivations, footnotes, side remarks, afterword, and source notes; expand section-by-section before counting as full. |
| `sources/usaco/usaco-nocow-solutions.tex` | 47 | Reviewed as A4 solution-note anthology. Companion note covers the USACO Training problem list and main ideas, but compresses alternate explanations, detailed derivations, sample details, and long source commentary into short per-problem notes. |
| `sources/dynamic-programming/tree-dp-selected-topics-gu-yihong.tex` | 142 | Reviewed as Beamer overlay deck: about 40 logical slides. Companion note keeps the DP states, transitions and examples. |
| `sources/dynamic-programming/dp-optimization-tang-wenbin.tex` | 23 | Reviewed as PowerPoint slide deck. Companion note keeps the LIS, Fibonacci subsequence, Painting the Balls, Divide, and quadrangle-inequality examples. |
| `sources/dynamic-programming/intro-digit-dp.tex` | 26 | Reviewed as image-only slide deck. Companion note covers the contents-page topics: HDU2089, HDU3652, URAL1057, `test-09-07-p1`, SPOJ Sorted Bit Sequence, and references. |
| `sources/dynamic-programming/state-compression-zhou-wei.tex` | 16 | Reviewed as A4 Word/PDF article whose available source appears truncated on page 16. Translation is a clean companion summary and even adds a conclusion not present in the available PDF; full repair needs the complete source or a clearly partial-source translation. |
| `sources/dynamic-programming/resource-allocation-dp-lou-tiancheng.tex` | 17 | Reviewed as slide deck. Companion note covers machine allocation, system reliability, fast-food production, shopping offers, and Jinming's budget. |
| `sources/data-structure/link-cut-trees.tex` | 81 | Reviewed as Word-exported A4 tutorial. Companion note preserves definitions, core operations, Splay details, practice-problem ideas, and complexity, but abridges walkthrough figures, full statements, sample I/O, and complete implementations. |
| `sources/graph-theory/making-graphs-into-trees-immortalco-wronganswer.tex` | 172 | Reviewed as Beamer overlay deck: about 51 logical slides. Companion note keeps DFS/BFS/cactus concepts and describes omitted figures in prose. |
| `sources/graph-theory/bipartite-graph-he-zhenhao.tex` | 22 | Reviewed as slide deck. Companion note covers the seven listed bipartite-graph topics; missing attached code is a code-template exception. |
| `sources/graph-theory/classic-network-flow-tutorial.tex` | 51 | Reviewed as slide deck. Companion note rewrites transport, max-flow, bounded-flow, min-cost-flow, worked examples, and homework slides as prose. |
| `sources/graph-theory/interval-chordal-perfect-graphs.tex` | 46 | Reviewed as Impress slide deck. Companion note covers interval graphs, coloring/clique, PEO, chordal recognition, interval recognition, PQ-tree, and perfect graphs. |
| `sources/graph-theory/network-flow-selected-problems-li-yuliang.tex` | 30 | Reviewed as Impress slide deck. Companion note expands the same sequence of flow-modeling examples and describes omitted figures in prose. |
| `sources/english/game-theory-ferguson-impartial-games.tex` | 46 | Reviewed as English lecture note companion. Theory chapters are translated, while long exercise lists are explicitly omitted or summarized. |
| `sources/data-structure/suffix-automaton-chen-lijie.tex` | 57 | Reviewed as slide deck with diagram/code-image pages. Companion note reconstructs the SAM construction and applications in lecture order. |
| `sources/others/pb-ds-in-oi-yu-jiping.tex` | 186 | Reviewed as slide deck with damaged text extraction. Companion note is self-contained and keeps the interfaces, code snippets and performance tables. |
| `sources/others/cdq-divide-and-conquer-introduction.tex` | 74 | Repaired after OCR of pages 51--74; companion note now includes submatrix k-th, ZJOI2013 K-th Query, HNOI2010 City, and FJOI2012 Point. |
| `sources/others/noi2016-wilderness-computation-solution.tex` | 42 | Reviewed as Beamer solution deck. Companion note keeps the operation table, scoring table, ten tests, and explicit notes for visual-only slides. |
| `sources/others/game-theory-li-xiaoxiao.tex` | 60 | Reviewed as slide deck. Companion note keeps the impartial-game definitions, Sprague--Grundy examples, and airplane-game DP discussion. |
| `sources/mathematics/linear-programming-simplex-wu-yifan.tex` | 40 | Reviewed as Beamer slide deck. Companion note keeps standard/slack forms, simplex pivots, Bland rule, duality, network flow, and BZOJ3876. |
| `sources/ioi/2003-wu-yu-symmetric-2sat.tex` | 24 | Reviewed as rasterized slide deck. Companion note keeps the Peaceful Commission example, implication graph symmetry, and construction algorithm. |
| `sources/ioi/2002/jin-kai-network-flow-applications.tex` | 28 | Reviewed as PowerPoint-style slide deck. Companion note covers the four network-flow examples and preserves the source's limitation for the CTSC2001 Agent statement. |
| `sources/ioi/2008/matrix-multiplication-applications-yu-huacheng-slides.tex` | 44 | Reviewed as slide companion for the matrix-multiplication paper. Core formulas and periodic-transition method are preserved. |
| `sources/ioi/2009-jin-bin-euclidean-algorithm-slides.tex` | 77 | Reviewed as slide companion. The source has a separate 14-page paper translation; this note keeps the slide-level Euclidean-algorithm examples. |
| `sources/ioi/2009-zhou-erjin-estimation-functions-slides.tex` | 36 | Reviewed as Impress slide deck. Companion note keeps search heuristics, DP optimization, near-optimal solution examples, and A/A* appendix material. |

## Explicitly Acceptable Short Files

- Code templates are not part of the translation quality target. The manifest
  marks source notebooks under `模板 TEMPLATES/` as `code-template` when the
  useful Vietnamese work is a translated index, heading map, or light notes
  around preserved code.
- PowerPoint-only files may remain concise companion notes when slide text is
  limited or heavily image-based, provided the file says that clearly.
- Temporary Microsoft Word lock files such as `~$*.doc` can remain short
  explanatory stubs.

## Diagram and Caption Quality

- Do not leave a standalone translated image caption when the image itself is
  omitted; either recreate/import the figure, or fold the useful visual
  information into prose that says it is a description of the original figure.
- Existing caption-only passages in older translated files should be treated as
  proofreading issues when those files are revisited.

## Audit Method

The skim used:

- `MANIFEST.csv` page counts compared with TeX line counts;
- searches for phrases such as `mục lục`, `Ghi chú về trích xuất`, `mojibake`,
  `OCR`, and `Bản LaTeX này`;
- spot checks with `pdftotext -layout`;
- a Tesseract sample on `国家集训队2022论文集.pdf`, which confirmed OCR can
  recover usable but noisy Chinese text.
