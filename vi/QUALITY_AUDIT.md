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
| `sources/dynamic-programming/tree-dp-selected-topics-gu-yihong.tex` | 142 | Reviewed as Beamer overlay deck: about 40 logical slides. Companion note keeps the DP states, transitions and examples. |
| `sources/dynamic-programming/dp-optimization-tang-wenbin.tex` | 23 | Reviewed as PowerPoint slide deck. Companion note keeps the LIS, Fibonacci subsequence, Painting the Balls, Divide, and quadrangle-inequality examples. |
| `sources/dynamic-programming/intro-digit-dp.tex` | 26 | Reviewed as image-only slide deck. Companion note covers the contents-page topics: HDU2089, HDU3652, URAL1057, `test-09-07-p1`, SPOJ Sorted Bit Sequence, and references. |
| `sources/dynamic-programming/resource-allocation-dp-lou-tiancheng.tex` | 17 | Reviewed as slide deck. Companion note covers machine allocation, system reliability, fast-food production, shopping offers, and Jinming's budget. |
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
