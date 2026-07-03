# Translation Quality Audit

This audit is separate from `MANIFEST.md`. The manifest tracks whether a source
document has a Vietnamese LaTeX file; it does not prove that the file is a full
translation.

For annual national training-team collections, `QUALITY_WORKLIST.md` expands
this audit into an article-by-article queue generated from the translated
tables of contents.

## High-Confidence Undertranslated Files

These files currently compile, but they are not full translations of their
source documents.

| Priority | Translation | Source pages | Current state | Extraction status | Required work |
| ---: | --- | ---: | --- | --- | --- |
| 1 | `sources/ioi/2013-national-training-team-collection.tex` | 137 | ToC plus first nine articles translated | ToC is readable; body required OCR due mojibake text layer | Continue OCR-backed translation from article 10 onward. |
| 2 | `sources/ioi/2014-national-training-team-collection.tex` | 228 | ToC plus first nine articles translated | ToC is readable; body required OCR due mojibake text layer | Continue OCR-backed translation from article 10 onward. |
| 3 | `sources/ioi/2016-national-training-team-collection.tex` | 234 | ToC plus first nine articles translated | ToC is readable; body required OCR due mojibake text layer | Continue OCR-backed translation from article 10 onward. |
| 4 | `sources/ioi/2015-national-training-team-collection.tex` | 291 | ToC plus first nine articles translated | `pdftotext` is mojibake even near the ToC; OCR works with visual checks | Continue OCR-backed translation from article 10 onward. |
| 5 | `sources/ioi/2023-national-training-team-collection.tex` | 249 | ToC plus first twelve articles translated | `pdftotext` extracts readable Unicode Chinese | Continue from article 13 onward. |
| 6 | `sources/ioi/2024-national-training-team-collection.tex` | 424 | ToC plus first article translated | Body text layer is noisy; OCR works but formulas need visual checks | Continue with OCR-backed article translations. |
| 7 | `sources/ioi/2025-national-training-team-collection.tex` | 168 | ToC plus first article translated | `pdftotext` is readable but two-up layout interleaves pages | Continue from article 2 onward, splitting/cropping pages where needed. |

## Article-Coverage Complete Annual Collections

These annual collections now have a translated section for every ToC article.
They may still need proofreading of formulas, OCR-heavy passages, and diagrams,
but they should not be counted as ToC-only or partially covered collections.

| Translation | Source pages | Current state | Notes |
| --- | ---: | --- | --- |
| `sources/ioi/2017-national-training-team-collection.tex` | 204 | ToC plus all fifteen articles translated | Final genome-reconstruction report translated from physical PDF pages 192--204. |
| `sources/ioi/2018-national-training-team-collection.tex` | 210 | ToC plus all fifteen articles translated | Final Euler graph generation/counting article translated from physical PDF pages 194--210. |
| `sources/ioi/2019-national-training-team-collection.tex` | 231 | ToC plus all fifteen articles translated | Final Young tableau article translated after filtering watermark/header noise. |
| `sources/ioi/2020-national-training-team-collection.tex` | 196 | ToC plus all fourteen articles translated | Proofread mathematical notation and examples when polishing. |
| `sources/ioi/2022-national-training-team-collection.tex` | 246 | ToC plus all fourteen articles translated | OCR-backed collection; proofread formulas, pseudocode, and diagram descriptions. |

## Large Reference PDFs That Are Only Notes

These are not IOI team reports, but they also should not be counted as full
book translations.

| Translation | Source pages | Current state | Recommendation |
| --- | ---: | --- | --- |
| `sources/english/introduction-to-algorithms-3e-clrs.tex` | 1313 | Book metadata and chapter-structure note | Either mark as reference-index only or translate selected chapters explicitly. |
| `sources/english/computer-systems-programmers-perspective-3e.tex` | 1120 | Book metadata and chapter-structure note | Keep as reference-index unless the project scope expands beyond OI texts. |
| `sources/english/concrete-mathematics-graham-knuth-patashnik.tex` | 670 | Book metadata and chapter-structure note | Translate selected chapters if needed for math background. |
| `sources/english/a-probability-path-resnick.tex` | 459 | Book metadata and chapter-structure note | Translate selected probability chapters if needed. |
| `sources/english/data-structures-network-algorithms-tarjan.tex` | 142 | ToC/preface-focused note | Candidate for full translation; source is shorter and relevant. |
| `sources/usaco/usaco-ten-year-problem-anthology-v10.tex` | 266 | Preface and recovered index only | Needs OCR or replacement text before full problem translation. |

## Lower-Confidence Compression Suspects

These files have low line-per-page ratios. Some may be acceptable condensed
translations, but they should be reviewed after the high-confidence items.

| Translation | Source pages | Notes |
| --- | ---: | --- |
| `sources/dynamic-programming/tree-dp-selected-topics-gu-yihong.tex` | 142 | Short for source size; verify against PDF. |
| `sources/graph-theory/making-graphs-into-trees-immortalco-wronganswer.tex` | 172 | Short for source size; verify against PDF. |
| `sources/others/pb-ds-in-oi-yu-jiping.tex` | 186 | Short for source size; likely condensed. |
| `sources/ioi/2008/matrix-multiplication-applications-yu-huacheng-slides.tex` | 44 | PDF slide deck; may be acceptable as companion, but mark as such. |
| `sources/ioi/2009-jin-bin-euclidean-algorithm-slides.tex` | 77 | PDF slide deck; may be acceptable as companion, but mark as such. |

## Explicitly Acceptable Short Files

- Code templates are not part of the translation quality target.
- PowerPoint-only files may remain concise companion notes when slide text is
  limited or heavily image-based, provided the file says that clearly.
- Temporary Microsoft Word lock files such as `~$*.doc` can remain short
  explanatory stubs.

## Audit Method

The skim used:

- `MANIFEST.csv` page counts compared with TeX line counts;
- searches for phrases such as `mục lục`, `Ghi chú về trích xuất`, `mojibake`,
  `OCR`, and `Bản LaTeX này`;
- spot checks with `pdftotext -layout`;
- a Tesseract sample on `国家集训队2022论文集.pdf`, which confirmed OCR can
  recover usable but noisy Chinese text.
