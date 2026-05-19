# Thesis V2 (Grammar-Focused) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write a complete LaTeX thesis using the UET template, focused on grammar engineering for SQLite fuzzing (no bandit/RL), with two research questions (CVE rediscovery + new bug discovery).

**Architecture:** Copy UET template to `docs/thesis/v2/`, adapt `thesis.tex` master document, write 4 chapters + conclusion + front matter. Reuse ~50% from old thesis at `docs/thesis/content/`, stripping all bandit/RL content. All content in English except Vietnamese cover and front matter labels.

**Tech Stack:** LaTeX (report class, 13pt, natbib, tikz), BibTeX

**Spec:** `docs/superpowers/specs/2026-05-11-thesis-v2-grammar-focused-design.md`
**Template:** `docs/thesis/template/`
**Old thesis:** `docs/thesis/content/`
**Output:** `docs/thesis/v2/`

---

### Task 1: Scaffold directory and master document

**Files:**
- Create: `docs/thesis/v2/thesis.tex`
- Create: `docs/thesis/v2/figures/` (directory)
- Create: `docs/thesis/v2/chapters/` (directory)

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p docs/thesis/v2/figures docs/thesis/v2/chapters
cp docs/thesis/template/figures/uet.jpg docs/thesis/v2/figures/
```

- [ ] **Step 2: Write thesis.tex master document**

Copy from `docs/thesis/template/thesis.tex` and adapt: change chapter includes to match our file names, keep all Vietnamese TOC/LOF/LOT labels, keep 13pt font, natbib, tikz, geometry settings. Remove the C5 chapter include. Keep `\input{chapters/c1/c1_introduction}` style paths but flatten to `chapters/c1_introduction` (no subdirs per chapter).

The master document must include these chapters in order:
1. `chapters/acknowledgement`
2. `chapters/assurance`
3. `chapters/abstract_vi`
4. `chapters/abstract_en`
5. `chapters/glossary`
6. `chapters/c1_introduction`
7. `chapters/c2_background`
8. `chapters/c3_method`
9. `chapters/c4_experiments`
10. `chapters/conclusion`

```latex
\documentclass[a4paper,13pt]{report}
\usepackage[utf8]{vietnam}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{xspace}
\usepackage[font=small]{caption}
\usepackage{booktabs}
\usepackage[unicode]{hyperref}
\usepackage[left=3cm,right=2cm,top=2.5cm,bottom=3cm]{geometry}
\usepackage{titlesec}
\usepackage{scrextend}
\usepackage{enumerate}
\usepackage{url}
\usepackage{tikz}
\usepackage{float}
\usepackage{afterpage}
\usepackage{multirow}
\usepackage{sectsty}
\usepackage{tocloft,calc}
\usepackage{listings}
\usepackage{makecell}
\usepackage[sort&compress]{natbib}
\usetikzlibrary{calc}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{subcaption}
\usepackage[flushleft]{threeparttable}
\usepackage{perpage}
\MakePerPage{footnote}
\PassOptionsToPackage{table}{xcolor}

\def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
\let\endchangemargin=\endlist

\changefontsizes{13pt}
\bibliographystyle{unsrt}

\makeatletter
\def\l@figure{\@dottedtocline{1}{1em}{2.2em}}
\def\l@table{\@dottedtocline{1}{1em}{2.2em}}
\renewcommand*{\ALG@name}{Algorithm}
\makeatother

\sectionfont{\fontsize{15}{15}\selectfont}
\subsectionfont{\fontsize{13}{15}\selectfont}

\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}{\chaptertitlename\ \thechapter}{0pt}{\LARGE}
\titlespacing*{\chapter}{0cm}{-\topskip}{0pt}[0pt]

\renewcommand{\baselinestretch}{1.3}
\renewcommand{\cftchappresnum}{Chapter }
\AtBeginDocument{\addtolength\cftchapnumwidth{\widthof{\bfseries Chapter }}}
\setlength{\parskip}{0.4em}
\setlength{\parindent}{0pt}

\title{Grammar-based Greybox Fuzzing for DBMS Vulnerability Detection}
\author{Nguyen Viet Kien}

\newcommand{\argmax}{\arg\!\max}

\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}
\definecolor{darkblue}{rgb}{0.0,0.0,0.6}
\definecolor{lightblue}{rgb}{0.0,0.0,0.9}
\definecolor{cyan}{rgb}{0.0,0.6,0.6}
\definecolor{darkred}{rgb}{0.6,0.0,0.0}
\definecolor{bg_gray}{RGB}{242, 242, 235}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\renewcommand{\lstlistingname}{Listing}
\newcommand{\cev}[1]{\reflectbox{\ensuremath{\vec{\reflectbox{\ensuremath{#1}}}}}}

\lstset{
  basicstyle=\ttfamily\footnotesize,
  columns=fullflexible,
  showstringspaces=false,
  numbers=left,
  numberstyle=\small\color{gray},
  stepnumber=1,
  numbersep=5pt,
  backgroundcolor=\color{bg_gray},
  showspaces=false,
  showstringspaces=false,
  showtabs=false,
  frame=none,
  rulecolor=\color{black},
  tabsize=2,
  captionpos=b,
  breaklines=true,
  breakatwhitespace=false,
  title=\lstname,
  commentstyle=\color{gray}\upshape
}

\begin{document}
\input{cover}\newpage\cleardoublepage

\input{chapters/acknowledgement}\newpage\cleardoublepage
\input{chapters/assurance}\newpage\cleardoublepage
\input{chapters/abstract_vi}\newpage\cleardoublepage
\input{chapters/abstract_en}\newpage\cleardoublepage
\addcontentsline{toc}{chapter}{Contents}
\tableofcontents\newpage\cleardoublepage

\newpage
\addcontentsline{toc}{chapter}{\listfigurename}
\listoffigures\cleardoublepage

\newpage
\addcontentsline{toc}{chapter}{\listtablename}
\listoftables

\newpage
\input{chapters/glossary}\newpage\cleardoublepage

\setcounter{page}{1}
\pagenumbering{arabic}

\input{chapters/c1_introduction}\newpage\cleardoublepage
\input{chapters/c2_background}\newpage\cleardoublepage
\input{chapters/c3_method}\newpage\cleardoublepage
\input{chapters/c4_experiments}\newpage\cleardoublepage
\input{chapters/conclusion}\newpage\cleardoublepage

\phantomsection
\addcontentsline{toc}{chapter}{References}
\bibliography{references}\newpage\cleardoublepage
\bibliographystyle{plain}
\end{document}
```

- [ ] **Step 3: Verify directory exists and file written**

```bash
ls -la docs/thesis/v2/thesis.tex docs/thesis/v2/figures/uet.jpg
```

Expected: both files exist.

- [ ] **Step 4: Commit**

```bash
git add docs/thesis/v2/
git commit -m "docs(thesis-v2): scaffold directory and master document"
```

---

### Task 2: Cover page and front matter

**Files:**
- Create: `docs/thesis/v2/cover.tex`
- Create: `docs/thesis/v2/chapters/acknowledgement.tex`
- Create: `docs/thesis/v2/chapters/assurance.tex`
- Create: `docs/thesis/v2/chapters/abstract_vi.tex`
- Create: `docs/thesis/v2/chapters/abstract_en.tex`
- Create: `docs/thesis/v2/chapters/glossary.tex`

- [ ] **Step 1: Write cover.tex**

Three cover pages (Vietnamese page 1, Vietnamese page 2 with supervisor, English page). Use template structure from `docs/thesis/template/cover.tex`. Fill in:
- Student name: Nguyễn Việt Kiên / Nguyen Viet Kien
- Title Vietnamese: PHƯƠNG PHÁP KIỂM THỬ MỜ DỰA TRÊN NGỮ PHÁP CHO PHÁT HIỆN LỖ HỔNG TỰ ĐỘNG TRONG SQLITE
- Title English: GRAMMAR-BASED GREYBOX FUZZING FOR AUTOMATED VULNERABILITY DISCOVERY IN SQLITE
- Supervisor: TS. Nguyễn Đức Anh / Dr. Nguyen Duc Anh
- Year: 2026
- Major: Công nghệ thông tin / Information Technology

```latex
% Cover Vietnamese 1
\pagenumbering{gobble}
\begin{center}
    \begin{tikzpicture}[overlay,remember picture]
        \draw [line width=3pt,rounded corners=0pt]
            ($ (current page.north west) + (25mm,-25mm) $)
            rectangle
            ($ (current page.south east) + (-15mm,25mm) $);
        \draw [line width=1pt,rounded corners=0pt]
            ($ (current page.north west) + (26.5mm,-26.5mm) $)
            rectangle
            ($ (current page.south east) + (-16.5mm,26.5mm) $);
    \end{tikzpicture}
    \\[1mm]
    \textbf{ĐẠI HỌC QUỐC GIA HÀ NỘI\\TRƯỜNG ĐẠI HỌC CÔNG NGHỆ}\\[1cm]
    \includegraphics[width=0.2\linewidth]{figures/uet}\\[0.3cm]
    \textbf{Nguyễn Việt Kiên}
    \\[2cm]

    \large{\textbf{PHƯƠNG PHÁP KIỂM THỬ MỜ DỰA TRÊN NGỮ PHÁP\\CHO PHÁT HIỆN LỖ HỔNG TỰ ĐỘNG TRONG SQLITE}}
    \\[2.6cm]
    \normalsize{\textbf{KHOÁ LUẬN TỐT NGHIỆP
        \\[2mm]
    Ngành: Công nghệ thông tin}}

    \vfill
    \textbf{HÀ NỘI - 2026}
    \vspace{10mm}
\end{center}

% Cover Vietnamese 2 (with supervisor)
\begin{center}
    \begin{tikzpicture}[overlay,remember picture]
    \draw [line width=3pt,rounded corners=0pt]
        ($ (current page.north west) + (25mm,-25mm) $)
        rectangle
        ($ (current page.south east) + (-15mm,25mm) $);
    \draw [line width=1pt,rounded corners=0pt]
        ($ (current page.north west) + (26.5mm,-26.5mm) $)
        rectangle
        ($ (current page.south east) + (-16.5mm,26.5mm) $);
    \end{tikzpicture}
    \\[1mm]
    \textbf{ĐẠI HỌC QUỐC GIA HÀ NỘI\\TRƯỜNG ĐẠI HỌC CÔNG NGHỆ}
    \\[1cm]
    \includegraphics[width=0.2\linewidth]{figures/uet}
    \\[0.3cm]
    \textbf{NGUYỄN VIỆT KIÊN}
    \\[2cm]

    \large{\textbf{PHƯƠNG PHÁP KIỂM THỬ MỜ DỰA TRÊN NGỮ PHÁP\\CHO PHÁT HIỆN LỖ HỔNG TỰ ĐỘNG TRONG SQLITE}}
    \\[2.6cm]
    \normalsize{\textbf{KHOÁ LUẬN TỐT NGHIỆP
        \\[2mm]
    Ngành: Công nghệ thông tin}}
\end{center}
\vspace{16mm}
\hspace*{12mm}\textbf{ Cán bộ hướng dẫn: TS. Nguyễn Đức Anh}
\vfill
\begin{center}
    \textbf{HÀ NỘI - 2026}
    \vspace{10mm}
\end{center}

% Cover English
\begin{center}
    \begin{tikzpicture}[overlay,remember picture]
    \draw [line width=3pt,rounded corners=0pt]
        ($ (current page.north west) + (25mm,-25mm) $)
        rectangle
        ($ (current page.south east) + (-15mm,25mm) $);
    \draw [line width=1pt,rounded corners=0pt]
        ($ (current page.north west) + (26.5mm,-26.5mm) $)
        rectangle
        ($ (current page.south east) + (-16.5mm,26.5mm) $);
    \end{tikzpicture}
    \\[1mm]
    \textbf{VIETNAM NATIONAL UNIVERSITY, HANOI\\UNIVERSITY OF ENGINEERING AND TECHNOLOGY}
    \\[1cm]
    \includegraphics[width=0.2\linewidth]{figures/uet}
    \\[0.3cm]
    \textbf{Nguyen Viet Kien}
    \\[2cm]

    \textbf{GRAMMAR-BASED GREYBOX FUZZING FOR\\AUTOMATED VULNERABILITY DISCOVERY IN SQLITE}
    \\[2.6cm]
    \textbf{BACHELOR'S THESIS
        \\[2mm]
        Major: Information Technology}
\end{center}
\vspace{16mm}
\hspace*{12mm}\textbf{ Supervisor: Dr. Nguyen Duc Anh}
\vfill
\begin{center}
    \textbf{HANOI - 2026}
    \vspace{4mm}
\end{center}
```

- [ ] **Step 2: Write acknowledgement.tex**

```latex
\begin{center}
\textbf{\large{Acknowledgements}}
\end{center}
\addcontentsline{toc}{chapter}{Acknowledgements}

First and foremost, I would like to express my sincere gratitude to the Faculty of Information Technology -- University of Engineering and Technology, Vietnam National University, Hanoi, for providing me with the opportunity to study, practice, and accumulate the essential knowledge that has built a solid foundation for me today.

Next, I would like to extend my deepest appreciation to Dr. Nguyen Duc Anh for his dedicated teaching, guidance, and support, as well as for giving me the opportunity to study and conduct research at the Software Quality Assurance Laboratory over the past year and during the completion of this thesis. His patient mentorship and wholehearted assistance have been a great source of motivation, helping me to improve myself and achieve the results I have today. I always feel extremely fortunate and proud to have been one of his students.

Finally, I would like to express my heartfelt thanks to all my classmates in K67CS for their constant companionship, support, and for creating such a joyful and connected learning environment throughout our years at the university.
```

- [ ] **Step 3: Write assurance.tex**

```latex
\setcounter{page}{1}
\pagenumbering{roman}
\begin{center}
\textbf{\large{Statement of Integrity}}
\end{center}
\addcontentsline{toc}{chapter}{Statement of Integrity}

I hereby declare that the graduation thesis entitled ``Grammar-based Greybox Fuzzing for DBMS Vulnerability Detection'' presented in this report is entirely my own work. The content does not involve any form of plagiarism or the use of others' results without proper citation. The proposed method in this thesis is the result of my own research, conducted under the supervision of Dr. Nguyen Duc Anh. I take full responsibility for any violations of the regulations of the University of Engineering and Technology, Vietnam National University, Hanoi.

\begin{flushright}
Ha Noi, June 2026
\end{flushright}

\begin{changemargin}{12cm}{2cm}
Student
\\[2cm]
\end{changemargin}

\begin{changemargin}{11cm}{2cm}
Nguyen Viet Kien
\end{changemargin}
```

- [ ] **Step 4: Write abstract_vi.tex**

```latex
\begin{center}
\textbf{\large{Tóm tắt}}
\end{center}
\addcontentsline{toc}{chapter}{Tóm tắt}

\begin{small}

Hệ quản trị cơ sở dữ liệu (DBMS) là thành phần hạ tầng quan trọng, và các lỗ hổng trong chúng đặt ra mối đe dọa an ninh nghiêm trọng. Phát hiện lỗ hổng tự động thông qua kiểm thử mờ (fuzzing) là một hướng tiếp cận đầy triển vọng, tuy nhiên các công cụ fuzzing dựa trên ngữ pháp hiện tại áp dụng lấy mẫu ngẫu nhiên đồng đều trên các luật sinh, dẫn đến lãng phí ngân sách đột biến vào các đường dẫn cú pháp có giá trị thấp.

Khóa luận này trình bày DBMS-Nautilus, một hệ thống kiểm thử mờ hộp xám dựa trên ngữ pháp nhắm vào SQLite. Một ngữ pháp nguyên thủy cấu trúc gồm 520 luật sinh mã hóa các mẫu SQL được biết là kích hoạt các lớp lỗ hổng -- bao gồm tràn số nguyên, sử dụng sau giải phóng, và lỗi bộ nhớ -- mà không mã hóa cứng các đầu vào chứng minh khái niệm cụ thể. Ngữ pháp phát triển qua bốn phiên bản (v3.0 đến v3.3), mỗi phiên bản được cải tiến dựa trên bằng chứng từ phân tích phủ mã và sự cố.

Thực nghiệm trên 4 phiên bản SQLite chứa 6 CVE đã xác nhận cho thấy DBMS-Nautilus phát hiện lại 3 trong 6 CVE mục tiêu thông qua tổ hợp ngữ pháp, và phát hiện thêm 7 lớp lỗi mới chưa được báo cáo trước đó trên 89 mẫu sự cố duy nhất. Phân tích khoảng trống ngữ pháp cho thấy 4 trong 6 CVE không thể đạt được cho đến khi các nguyên thủy cấu trúc cho hàm cửa sổ và cột tự tham chiếu được thêm vào phiên bản v3.2, chứng minh rằng thiết kế ngữ pháp là yếu tố quyết định hàng đầu cho khả năng phát hiện lỗ hổng.

\vspace*{1cm}
\textbf{Từ khóa}: Kiểm thử mờ dựa trên ngữ pháp, Kiểm thử mờ hộp xám, An ninh DBMS, Phát hiện lỗ hổng, SQLite
\end{small}
```

- [ ] **Step 5: Write abstract_en.tex**

```latex
\begin{center}
\textbf{\large{Abstract}}
\end{center}
\addcontentsline{toc}{chapter}{Abstract}

\begin{small}

Database management systems (DBMS) are critical infrastructure components, and their vulnerabilities represent serious security threats. Automated vulnerability detection through fuzzing is a promising approach, but existing grammar-based fuzzers apply uniform random sampling over production rules, wasting mutation budget on low-value syntactic paths and failing to prioritize the structural patterns most likely to expose bugs.

This thesis presents DBMS-Nautilus, a grammar-based greybox fuzzing system targeting SQLite. A structural primitives grammar of 520 rules encodes SQL patterns known to trigger vulnerability classes---including integer overflow in expression evaluation, use-after-free in query planner optimizations, and null pointer dereference in column resolution---without hardcoding specific proof-of-concept inputs. The grammar evolved through four versions (v3.0 to v3.3), each refined based on evidence from coverage analysis and crash investigation.

Experiments across 4 SQLite versions containing 6 known CVEs show that DBMS-Nautilus rediscovers 3 of the 6 target CVEs through compositional grammar generation, and discovers 7 additional previously unreported bug classes across 89 unique crash instances. A grammar gap analysis reveals that 4 of the 6 target CVEs were unreachable until structural primitives for window functions and self-referential generated columns were added in grammar version 3.2, demonstrating that grammar design is the dominant factor for vulnerability reachability.

\vspace*{1cm}
\textbf{Keywords}: Grammar-based Fuzzing, Greybox Fuzzing, DBMS Security, Vulnerability Detection, SQLite
\end{small}
```

- [ ] **Step 6: Write glossary.tex**

```latex
\chapter*{List of Abbreviations}
\addcontentsline{toc}{chapter}{List of Abbreviations}

\begin{tabular}{|m{2.0cm}|m{5.4cm}|m{6.3cm}|}
    \hline
\thead{Abbreviation} & \thead{Full Term} & \thead{Description} \\
    \hline
AFL & American Fuzzy Lop & Coverage-guided greybox fuzzer \\    \hline
ASan & AddressSanitizer & Memory error detector \\    \hline
CFG & Context-Free Grammar & Formal grammar where rules map non-terminals to symbol sequences \\    \hline
CVE & Common Vulnerabilities and Exposures & Unique identifier for publicly disclosed vulnerabilities \\    \hline
DBMS & Database Management System & Software for managing structured data \\    \hline
DML & Data Manipulation Language & SQL statements for data modification (INSERT, UPDATE, DELETE) \\    \hline
DDL & Data Definition Language & SQL statements for schema definition (CREATE, ALTER, DROP) \\    \hline
FTS & Full-Text Search & SQLite virtual table module for text indexing \\    \hline
NVD & National Vulnerability Database & US government repository of CVE data \\    \hline
UBSan & UndefinedBehaviorSanitizer & Undefined behavior detector \\    \hline
VDBE & Virtual Database Engine & SQLite bytecode execution engine \\    \hline
\end{tabular}
```

- [ ] **Step 7: Commit**

```bash
git add docs/thesis/v2/cover.tex docs/thesis/v2/chapters/
git commit -m "docs(thesis-v2): add cover pages and front matter"
```

---

### Task 3: References bibliography

**Files:**
- Create: `docs/thesis/v2/references.bib`

- [ ] **Step 1: Write references.bib**

Start from `docs/thesis/content/references.bib`. Remove `exp3` and `mannwhitney` entries (bandit/stats — not used in v2). Keep all fuzzing, DBMS, sanitizer, and CVE entries. Add new entries for SQLRight, Griffin, SQLancer, DynSQL, MOPT, EcoFuzz.

```bibtex
% ============================================================
% references.bib — Bibliography for DBMS-Nautilus thesis v2
% ============================================================

% --------------- Grammar-based / coverage-guided fuzzing ---------------

@inproceedings{nautilus,
  author    = {Cornelius Aschermann and Tommaso Frassetto and Thorsten Holz
               and Patrick Jauernig and Christoph Cloosters and Ahmad-Reza Sadeghi},
  title     = {{NAUTILUS}: Fishing for Deep Bugs with Grammars},
  booktitle = {Proceedings of the Network and Distributed System Security Symposium (NDSS)},
  year      = {2019},
  publisher = {Internet Society},
}

@misc{afl,
  author       = {Michal Zalewski},
  title        = {American Fuzzy Lop},
  year         = {2014},
  howpublished = {\url{https://lcamtuf.coredump.cx/afl/}},
}

@inproceedings{superion,
  author    = {Junjie Wang and Bihuan Chen and Lei Wei and Yang Liu},
  title     = {Superion: Grammar-Aware Greybox Fuzzing},
  booktitle = {Proceedings of the 41st International Conference on Software Engineering (ICSE)},
  year      = {2019},
  publisher = {IEEE / ACM},
  pages     = {724--735},
}

@inproceedings{grimoire,
  author    = {Tim Blazytko and Cornelius Aschermann and Moritz Schl{\"o}gel
               and Ali Nawrocki and Steffen Kornmaier and Thorsten Holz},
  title     = {{GRIMOIRE}: Synthesizing Structure while Fuzzing},
  booktitle = {Proceedings of the 28th USENIX Security Symposium},
  year      = {2019},
  publisher = {USENIX Association},
  pages     = {1985--2002},
}

@misc{libfuzzer,
  author       = {{LLVM Project}},
  title        = {{libFuzzer} -- a Library for Coverage-Guided Fuzz Testing},
  howpublished = {\url{https://llvm.org/docs/LibFuzzer.html}},
}

@inproceedings{mopt,
  author    = {Chenyang Lyu and Shouling Ji and Chao Zhang and Yuwei Li
               and Wei-Han Lee and Yu Song and Raheem Beyah},
  title     = {{MOPT}: Optimized Mutation Scheduling for Fuzzers},
  booktitle = {Proceedings of the 28th USENIX Security Symposium},
  year      = {2019},
  publisher = {USENIX Association},
  pages     = {1949--1966},
}

@inproceedings{ecofuzz,
  author    = {Tai Yue and Pengfei Wang and Yong Tang and Enze Wang and Bo Yu
               and Kai Lu and Xu Zhou},
  title     = {{EcoFuzz}: Adaptive Energy-Saving Greybox Fuzzing as a Variant
               of the Adversarial Multi-Armed Bandit},
  booktitle = {Proceedings of the 29th USENIX Security Symposium},
  year      = {2020},
  publisher = {USENIX Association},
  pages     = {2307--2324},
}

% --------------- Database fuzzing ---------------

@inproceedings{squirrel,
  author    = {Rui Zhong and Yongheng Chen and Hong Wen and Hangfan Zhang
               and Wenke Lee and Dinghao Wu and Peng Liu},
  title     = {Squirrel: Testing Database Management Systems with Language
               Validity and Coverage Feedback},
  booktitle = {Proceedings of the 2020 ACM SIGSAC Conference on Computer and
               Communications Security (CCS)},
  year      = {2020},
  publisher = {ACM},
  pages     = {955--970},
}

@misc{sqlsmith,
  author       = {Andreas Seltenreich},
  title        = {{SQLsmith}: A Random {SQL} Query Generator},
  year         = {2015},
  howpublished = {\url{https://github.com/anse1/sqlsmith}},
}

@inproceedings{sqlright,
  author    = {Rui Zhong and Yongheng Chen and Hong Hu and Hangfan Zhang
               and Wenke Lee and Dinghao Wu},
  title     = {{SQLRight}: Enabling Coverage-based SQL Fuzzing with
               Side-channel Analysis},
  booktitle = {Proceedings of the 31st USENIX Security Symposium},
  year      = {2022},
  publisher = {USENIX Association},
}

@inproceedings{griffin,
  author    = {Jie Fu and Jingzhou Fu and Qingchao Shen and Zhiyong Wu
               and Jianwei Zhuge},
  title     = {{Griffin}: Grammar-Free DBMS Fuzzing},
  booktitle = {Proceedings of the 37th IEEE/ACM International Conference on
               Automated Software Engineering (ASE)},
  year      = {2022},
  publisher = {ACM},
}

@inproceedings{sqlancer,
  author    = {Manuel Rigger and Zhendong Su},
  title     = {Testing Database Engines via Pivoted Query Synthesis},
  booktitle = {Proceedings of the 14th USENIX Symposium on Operating Systems
               Design and Implementation (OSDI)},
  year      = {2020},
  publisher = {USENIX Association},
  pages     = {667--682},
}

@inproceedings{dynsql,
  author    = {Zu-Ming Jiang and Jia-Ju Bai and Zhendong Su},
  title     = {{DynSQL}: Stateful Fuzzing for Database Management Systems
               with Complex and Valid SQL Query Generation},
  booktitle = {Proceedings of the 32nd USENIX Security Symposium},
  year      = {2023},
  publisher = {USENIX Association},
}

% --------------- Target software ---------------

@misc{sqlite,
  author       = {D. Richard Hipp and Dan Kennedy and Joe Mistachkin},
  title        = {{SQLite}},
  year         = {2000},
  note         = {Version 3.x},
  howpublished = {\url{https://www.sqlite.org/}},
}

% --------------- Sanitizers / oracles ---------------

@inproceedings{asan,
  author    = {Konstantin Serebryany and Derek Bruening and Alexander Potapenko
               and Dmitriy Vyukov},
  title     = {{AddressSanitizer}: A Fast Address Sanity Checker},
  booktitle = {Proceedings of the 2012 USENIX Annual Technical Conference (ATC)},
  year      = {2012},
  publisher = {USENIX Association},
  pages     = {309--318},
}

% --------------- Weighted sampling algorithm ---------------

@article{loadeddice,
  author  = {Michael D. Vose},
  title   = {A Linear Algorithm for Generating Random Numbers with a Given
             Distribution},
  journal = {IEEE Transactions on Software Engineering},
  volume  = {17},
  number  = {9},
  year    = {1991},
  pages   = {972--975},
}

% --------------- Survey ---------------

@article{fuzzingsurvey,
  author  = {Valentin J. M. Man{\`e}s and HyungSeok Han and Choongwoo Han
             and Sang Kil Cha and Manuel Egele and Edward J. Schwartz
             and Maverick Woo},
  title   = {The Art, Science, and Engineering of Fuzzing: {A} Survey},
  journal = {IEEE Transactions on Software Engineering},
  volume  = {47},
  number  = {11},
  year    = {2021},
  pages   = {2312--2331},
}

% --------------- CVE entries ---------------

@misc{cve201919646,
  author       = {{MITRE}},
  title        = {{CVE-2019-19646}},
  year         = {2019},
  howpublished = {\url{https://nvd.nist.gov/vuln/detail/CVE-2019-19646}},
  note         = {SQLite \texttt{expr.c} aggregate query infinite loop},
}

@misc{cve202013434,
  author       = {{MITRE}},
  title        = {{CVE-2020-13434}},
  year         = {2020},
  howpublished = {\url{https://nvd.nist.gov/vuln/detail/CVE-2020-13434}},
  note         = {SQLite \texttt{printf} integer overflow},
}

@misc{cve20209327,
  author       = {{MITRE}},
  title        = {{CVE-2020-9327}},
  year         = {2020},
  howpublished = {\url{https://nvd.nist.gov/vuln/detail/CVE-2020-9327}},
  note         = {SQLite generated column uninitialized pointer},
}

@misc{cve202013435,
  author       = {{MITRE}},
  title        = {{CVE-2020-13435}},
  year         = {2020},
  howpublished = {\url{https://nvd.nist.gov/vuln/detail/CVE-2020-13435}},
}

@misc{cve202013871,
  author       = {{MITRE}},
  title        = {{CVE-2020-13871}},
  year         = {2020},
  howpublished = {\url{https://nvd.nist.gov/vuln/detail/CVE-2020-13871}},
}

@misc{cve202015358,
  author       = {{MITRE}},
  title        = {{CVE-2020-15358}},
  year         = {2020},
  howpublished = {\url{https://nvd.nist.gov/vuln/detail/CVE-2020-15358}},
}
```

- [ ] **Step 2: Commit**

```bash
git add docs/thesis/v2/references.bib
git commit -m "docs(thesis-v2): add bibliography with DBMS testing tool references"
```

---

### Task 4: Chapter 1 — Introduction

**Files:**
- Create: `docs/thesis/v2/chapters/c1_introduction.tex`

**Source:** Adapt from `docs/thesis/content/chapters/c1_introduction.tex` (~40% reuse). Strip all bandit/RL motivation, reframe around grammar engineering. New RQs, new contributions.

- [ ] **Step 1: Write c1_introduction.tex**

Sections:
1. Context and Motivation (~2 pages): SQLite ubiquity, CVE persistence, byte-level fuzzer limitation, grammar-based fuzzer limitation (uniform sampling, no domain knowledge). Same opening paragraphs as old C1 but remove the bandit motivation paragraph.
2. Problem Statement (~0.5 page): Can a carefully engineered grammar with structural primitives improve vulnerability discovery? Two RQs.
3. Objectives and Scope (~0.5 page): (1) design structural primitives grammar, (2) build DBMS-Nautilus system, (3) evaluate on 4 SQLite versions.
4. Contributions (~0.5 page): (1) structural primitives methodology, (2) grammar evolution v3.0→v3.3, (3) empirical results: 3 CVEs + 7 new bug classes.
5. Thesis Organization (~0.5 page): paragraph pointing to each chapter.

Key changes from old C1:
- Remove paragraph about "adaptive rule selection strategies" from Section 1.1
- Replace "central research question" about bandit with two RQs about grammar effectiveness
- Remove second objective (bandit integration) and third objective (bandit vs uniform comparison)
- Replace three contributions (grammar, bandit, counterintuitive finding) with three grammar-focused contributions
- Update thesis organization to reflect new chapter structure (no bandit in C3, no bandit comparison in C4)

The full LaTeX content for this file should be written as a complete chapter. Reuse the first two paragraphs of the old C1 Section 1.1 (Context and Motivation) verbatim — they cover SQLite ubiquity and fuzzing fundamentals. Reuse the third paragraph about grammar-based fuzzing (Nautilus, Superion, Grimoire, Squirrel, SQLsmith). Then write a NEW fourth paragraph that transitions from "uniform sampling limitation" to "grammar design is the key challenge" instead of "adaptive rule selection."

For Section 1.2 (Problem Statement), write new content with two RQs:
- RQ1: Can DBMS-Nautilus rediscover existing CVEs through compositional grammar generation without embedding proof-of-concept inputs?
- RQ2: Can DBMS-Nautilus discover previously unreported bugs beyond known CVEs?

For Section 1.3 (Objectives), three objectives: (1) design structural primitives grammar, (2) implement DBMS-Nautilus with fork server + harness + triage, (3) empirical evaluation on 4 SQLite versions.

For Section 1.4 (Contributions): (1) structural primitives grammar methodology with zero PoC contamination, (2) grammar evolution v3.0→v3.3 driven by evidence, (3) empirical results — 3 CVEs rediscovered + 7 new bug classes + 89 unique crashes.

For Section 1.5 (Thesis Organization): brief paragraph for each chapter.

- [ ] **Step 2: Verify no bandit/RL references remain**

```bash
grep -i -E "bandit|reinforcement|RL|EXP3|multi-armed|exploration.exploitation|adaptive.*sampling|weight.*update" docs/thesis/v2/chapters/c1_introduction.tex
```

Expected: no output (no matches).

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c1_introduction.tex
git commit -m "docs(thesis-v2): write Chapter 1 — Introduction"
```

---

### Task 5: Chapter 2 — Background and Related Work

**Files:**
- Create: `docs/thesis/v2/chapters/c2_background.tex`

**Source:** Adapt from `docs/thesis/content/chapters/c2_background.tex` (~70% reuse). Remove Section 2.5 (Multi-Armed Bandit Algorithms) entirely. Remove bandit references from Section 2.7 (Related Work). Add DBMS testing tools section.

- [ ] **Step 1: Write c2_background.tex**

Sections (5 total):
1. **Software Vulnerabilities and CVEs** (~1.5 pages): Reuse old Section 2.1 verbatim. Includes Table of 6 target CVEs.
2. **Fuzzing** (~1.5 pages): Reuse old Section 2.2 verbatim. Covers black-box/white-box/greybox taxonomy, mutation vs generation, coverage feedback loop.
3. **Grammar-Based Fuzzing** (~2 pages): Reuse old Section 2.3 verbatim. CFG definition, derivation trees, tree mutations, Nautilus description, grammar DSL listing.
4. **Coverage-Guided Feedback** (~1.5 pages): Reuse old Section 2.4 verbatim. AFL fork server, edge coverage bitmap, coverage-guided selection, crash isolation.
5. **Sanitizers as Oracles** (~1 page): Reuse old Section 2.6 verbatim. ASan, UBSan, SQLITE_DEBUG assertions, oracle classification.
6. **Related Work** (~2.5 pages): Heavily rewrite old Section 2.7. Keep Nautilus, Superion, Grimoire, Squirrel, SQLsmith, AFL/libFuzzer paragraphs but remove all bandit references. Add new paragraphs for: SQLRight, Griffin, SQLancer, DynSQL. Add comparison table. Change final positioning paragraph to focus on grammar engineering instead of bandit integration.

The Related Work comparison table:

```latex
\begin{table}[htbp]
\caption{Comparison of DBMS fuzzing tools. DBMS-Nautilus is the only system combining grammar-based generation with domain-specific structural primitives for CVE-class vulnerability targeting.}
\label{tab:related-comparison}
\centering
\begin{tabular}{lccccc}
\toprule
\textbf{Tool} & \textbf{Grammar} & \textbf{Coverage} & \textbf{Semantic} & \textbf{Domain} & \textbf{Multi-DBMS} \\
\midrule
AFL~\cite{afl}            & No  & Yes & No  & No  & --- \\
SQLsmith~\cite{sqlsmith}  & Yes & No  & Yes & No  & Yes \\
Squirrel~\cite{squirrel}  & Yes & Yes & Yes & No  & Yes \\
SQLRight~\cite{sqlright}  & Yes & Yes & Yes & No  & Yes \\
Griffin~\cite{griffin}     & No  & Yes & No  & No  & Yes \\
SQLancer~\cite{sqlancer}  & Yes & No  & Yes & No  & Yes \\
DynSQL~\cite{dynsql}      & Yes & Yes & Yes & No  & Yes \\
Nautilus~\cite{nautilus}   & Yes & Yes & No  & No  & No  \\
\textbf{DBMS-Nautilus}     & Yes & Yes & No  & Yes & No  \\
\bottomrule
\end{tabular}
\end{table}
```

"Domain" column = domain-specific structural primitives (only DBMS-Nautilus has this). "Semantic" = type-aware generation.

Final positioning paragraph:
> This thesis positions DBMS-Nautilus at the intersection of grammar-based generation (Nautilus) and domain-specific vulnerability targeting. Unlike Squirrel and SQLRight, it does not require a full SQL parser; a Python-defined context-free grammar suffices. Unlike SQLsmith, it employs coverage-guided feedback. Unlike Griffin, it generates inputs from a grammar rather than mutating existing queries. The key novelty is the structural primitives grammar methodology: encoding CVE-triggering patterns as composable non-terminals that the fuzzer combines through random generation and mutation, enabling systematic rediscovery of known vulnerabilities and discovery of new ones.

- [ ] **Step 2: Verify no bandit/RL references remain**

```bash
grep -i -E "bandit|reinforcement|RL|EXP3|multi-armed|exploration.exploitation|adaptive.*sampling|weight.*update" docs/thesis/v2/chapters/c2_background.tex
```

Expected: no output.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c2_background.tex
git commit -m "docs(thesis-v2): write Chapter 2 — Background and Related Work"
```

---

### Task 6: Chapter 3 — DBMS-Nautilus: Design and Implementation

**Files:**
- Create: `docs/thesis/v2/chapters/c3_method.tex`

**Source:** Adapt from `docs/thesis/content/chapters/c3_method.tex` (~60% reuse). Remove Section 3.4 (Weighted Sampling with Bandit Policy) entirely — no Algorithm 1, no EXP3, no bandit formulation, no uniform baseline section. Add Section 3.4 Grammar Evolution as the core new content.

- [ ] **Step 1: Write c3_method.tex**

Sections (7 total):
1. **System Overview** (~2 pages): Reuse old Section 3.1 but simplify architecture diagram — remove "Weight Update (Bandit Policy)" node and its feedback arrow. Change the node to "Queue Update" and the arrow label to "new edges?" → "add to queue". Keep all 5 component descriptions (Grammar Engine, Fuzzer Coordinator, Fork Server, Harness, Triage Pipeline). Remove mention of "bandit policy described in Section 3.4" from Fuzzer Coordinator paragraph — replace with "the coordinator determines whether the input triggered new edge transitions in the coverage bitmap. If so, it adds the input to the queue for further mutation."

The simplified TikZ architecture diagram:

```latex
\begin{figure}[htbp]
\centering
\begin{tikzpicture}[
    node distance=1.8cm and 2.2cm,
    block/.style={rectangle, draw, rounded corners, minimum width=2.8cm, minimum height=1.0cm, text centered, align=center, font=\small},
    arrow/.style={->, >=stealth, thick},
    label/.style={font=\scriptsize, midway}
]
    \node[block] (grammar) {Grammar Rules\\(\texttt{grammartec/})};
    \node[block, right=of grammar] (sampling) {Weighted\\Sampling};
    \node[block, right=of sampling] (tree) {Tree Generation\\+ Mutation};
    \node[block, below=of tree] (unparse) {Unparse\\to SQL String};
    \node[block, below=of unparse] (forkserver) {Fork Server\\(\texttt{forksrv/})};
    \node[block, left=of forkserver] (harness) {SQLite Harness\\(ASan+UBSan)};
    \node[block, left=of harness] (coverage) {Coverage\\Bitmap (2\,MB)};
    \node[block, above=of coverage] (queue) {Queue Update};

    \draw[arrow] (grammar) -- (sampling) node[label, above] {rules};
    \draw[arrow] (sampling) -- (tree) node[label, above] {weights};
    \draw[arrow] (tree) -- (unparse) node[label, right] {parse tree};
    \draw[arrow] (unparse) -- (forkserver) node[label, right] {SQL text};
    \draw[arrow] (forkserver) -- (harness) node[label, above] {fork + exec};
    \draw[arrow] (harness) -- (coverage) node[label, above] {exit status};
    \draw[arrow] (coverage) -- (queue) node[label, left] {new edges?};
    \draw[arrow] (queue) -- (sampling) node[label, left] {retain input};
\end{tikzpicture}
\caption{Architecture of DBMS-Nautilus. Arrows indicate data flow direction. The coverage feedback loop retains inputs that discover new edges, building a corpus that guides subsequent generation toward unexplored program regions.}
\label{fig:architecture}
\end{figure}
```

2. **Structural Primitives Philosophy** (~1.5 pages): Reuse old Section 3.2.1 verbatim. Zero PoC contamination, three design constraints, CVE-2020-13434 example.

3. **Layer Decomposition** (~3 pages): Reuse old Section 3.2.2 verbatim. Layer 1 atoms, Layer 2 composed shapes. Keep all three code listings (Schema-Setup, Stress-Query, Boundary-Func-Call).

4. **Grammar Evolution** (~3 pages): NEW content — the core contribution section. This replaces the old bandit section. Contains:
   - Grammar version history table (v3.0→v3.3, 4 rows)
   - Narrative for each version transition:
     - v3.0→v3.1: FTS weight dominance problem. 92% crash monopoly → reduced S5 weight from 2.0 to 0.5.
     - v3.1→v3.2: Gap analysis. 4 CVEs unreachable → added 26 rules (window functions, self-ref genCol, count(), ORDER BY 3-term). CVE reachability from 2/6 to 6/6.
     - v3.2→v3.3: JSON/JSONB expansion. Targeting json.c in SQLite 3.53.0. Added Json-Key (4 rules), Json-Path (8 rules), Json-Literal (6 rules). Total 469→520 rules.
   - CVE reachability matrix table (grammar version × CVE)
   - Key insight paragraph: grammar evolution operates on two axes — weight tuning (probability distribution over existing rules) and structural expansion (boundaries of expressible input space). Both are necessary.

5. **Harness Construction** (~1.5 pages): Reuse old Section 3.5 verbatim. AFL fork server, simplified harness listing, compilation flags. Add brief mention of three harness types (afl/test/nosanit) from CLAUDE.md.

6. **Oracle Classification** (~0.5 page): Reuse old Section 3.5.3 (oracle table) verbatim.

7. **Triage Pipeline** (~2 pages): Reuse old Section 3.6 verbatim. Stack-hash dedup (Algorithm 2), CVE signature matching (Table of patterns), fidelity scoring, crash minimization.

- [ ] **Step 2: Verify no bandit/RL references remain**

```bash
grep -i -E "bandit|reinforcement|RL|EXP3|multi-armed|exploration.exploitation|adaptive.*sampling|Algorithm.*1|uniform.*baseline" docs/thesis/v2/chapters/c3_method.tex
```

Expected: no output.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "docs(thesis-v2): write Chapter 3 — DBMS-Nautilus Design and Implementation"
```

---

### Task 7: Chapter 4 — Experiments and Evaluation

**Files:**
- Create: `docs/thesis/v2/chapters/c4_experiments.tex`

**Source:** Mostly NEW content (~30% reuse from old C4). Completely new RQ structure. Reuse experimental setup parameters and crash data tables.

- [ ] **Step 1: Write c4_experiments.tex**

Sections (5 total):

1. **Experimental Setup** (~1.5 pages):
   - Hardware: Intel Core i7, 16GB RAM, Ubuntu 22.04
   - Toolchain: Rust 1.77, Clang 14, Python 3.13
   - Campaign parameters table (adapt from old Table 4.1 but remove "Sampling policies" row, remove "Total campaigns: 53" — use actual campaign count across all grammar versions)
   - Target SQLite versions: 3.30.1, 3.31.1, 3.32.0, 3.32.2 (4 versions, not 3 like old thesis)
   - Grammar versions: v3.0 through v3.3
   - Metrics: unique root causes (stack-hash top-5 dedup), edge coverage, crash count, CVE signature match
   - No statistical comparison section (no bandit vs uniform)

2. **RQ1: Can DBMS-Nautilus Rediscover Existing CVEs?** (~4 pages):

   Methodology paragraph: Run campaigns on 4 CVE-bearing SQLite versions using grammar versions v3.0 through v3.2. Check crash evidence against CVE signature library. Track which grammar version first enables each CVE to be found.

   Results table — CVE rediscovery summary:

   ```latex
   \begin{table}[htbp]
   \caption{CVE rediscovery results. Three of six target CVEs were rediscovered through compositional grammar generation. The ``First Grammar'' column indicates the earliest grammar version containing all required structural primitives.}
   \label{tab:cve-rediscovery}
   \centering
   \begin{tabular}{llllc}
   \toprule
   \textbf{CVE} & \textbf{Bug Class} & \textbf{Versions Found} & \textbf{First Grammar} & \textbf{Rediscovered} \\
   \midrule
   CVE-2020-13434 & BC003 & 3.30.1, 3.31.1, 3.32.0 & v3.0 & \checkmark \\
   CVE-2020-9327  & BC010 & 3.31.1 & v3.2 & \checkmark \\
   CVE-2020-13871 & BC002 & 3.30.1 & v3.2 & \checkmark \\
   CVE-2019-19646 & --- & --- & v3.0 & $\times$ \\
   CVE-2020-13435 & --- & --- & v3.2 & $\times$ \\
   CVE-2020-15358 & --- & --- & v3.2 & $\times$ \\
   \bottomrule
   \end{tabular}
   \end{table}
   ```

   CVE reachability matrix table (reuse from old RQ3 Table but add v3.0 and v3.3 columns):

   ```latex
   \begin{table}[htbp]
   \caption{Grammar evolution and CVE reachability. Checkmarks indicate the grammar version contains all required structural building blocks for the CVE.}
   \label{tab:cve-reachability}
   \centering
   \begin{tabular}{lcccc}
   \toprule
   \textbf{CVE} & \textbf{v3.0 (449)} & \textbf{v3.1 (449)} & \textbf{v3.2 (475)} & \textbf{v3.3 (520)} \\
   \midrule
   CVE-2019-19646 & \checkmark & \checkmark & \checkmark & \checkmark \\
   CVE-2020-13434 & \checkmark & \checkmark & \checkmark & \checkmark \\
   CVE-2020-9327  & $\times$ & $\times$ & \checkmark & \checkmark \\
   CVE-2020-13435 & $\times$ & $\times$ & \checkmark & \checkmark \\
   CVE-2020-13871 & $\times$ & $\times$ & \checkmark & \checkmark \\
   CVE-2020-15358 & $\times$ & $\times$ & \checkmark & \checkmark \\
   \midrule
   \textbf{Reachable} & 2/6 & 2/6 & 6/6 & 6/6 \\
   \bottomrule
   \end{tabular}
   \end{table}
   ```

   Case study paragraphs for each rediscovered CVE:
   - BC003 → CVE-2020-13434: integer overflow in `sqlite3_str_vappendf`. Found on 3 versions. Grammar's Boundary-Func-Call composes printf + INT32_MAX. 1501 crashes, 6 unique hashes.
   - BC010 → CVE-2020-9327: null pointer in `sqlite3Select`. Only found on 3.31.1. Requires 4 structural elements (genCol + VIEW + coalesce + JOIN). Only 1 crash found — demonstrates compositional rarity.
   - BC002 → CVE-2020-13871: misaligned access in `sqlite3WindowUnlinkFromSelect`. Found on 3.30.1 only. 265 crashes. Root cause is use-after-free in window function processing; UBSan reports as misaligned access.

   Discussion paragraph on unfound CVEs:
   - CVE-2019-19646: infinite loop, not a crash. Sanitizer oracle does not detect denial-of-service.
   - CVE-2020-13435: needs 5 simultaneous structural elements (NATURAL JOIN + coalesce + window OVER + UNIQUE + IN subquery). Combinatorial probability extremely low in 15-30 min campaigns.
   - CVE-2020-15358: INTERSECT in scalar subquery context. Grammar contains INTERSECT and subquery primitives but the specific composition has not been found in campaigns to date.

3. **RQ2: Can DBMS-Nautilus Discover New Bugs?** (~4 pages):

   Methodology paragraph: Analyze crash evidence archive for bug classes with no CVE signature match.

   Full bug class table (from crash registry):

   ```latex
   \begin{table}[htbp]
   \caption{All bug classes discovered by DBMS-Nautilus. Ten distinct bug classes were identified through stack-hash deduplication across all campaigns. Three match known CVEs; seven are previously unreported.}
   \label{tab:all-bugs}
   \centering
   \begin{tabular}{llllcr}
   \toprule
   \textbf{Class} & \textbf{Bug Type} & \textbf{Severity} & \textbf{Versions} & \textbf{CVE} & \textbf{Hashes} \\
   \midrule
   BC001 & Null ptr in sqlite3Fts5GetTokenizer & HIGH & 4 versions & --- & 4 \\
   BC002 & Misaligned access in sqlite3WindowUnlinkFromSelect & HIGH & 3.30.1 & CVE-2020-13871 & 1 \\
   BC003 & Signed int overflow in sqlite3\_str\_vappendf & MEDIUM & 3 versions & CVE-2020-13434 & 6 \\
   BC004 & Float cast overflow in alsoAnInt & LOW & 4 versions & --- & 42 \\
   BC005 & Signal 6 in sqlite3WindowListDelete & MEDIUM & 3.30.1 & --- & 4 \\
   BC006 & Null ptr in sqlite3AtoF & HIGH & 3.30.1 & --- & 1 \\
   BC007 & Null ptr in sqlite3Atoi64 & HIGH & 3.30.1 & --- & 1 \\
   BC008 & Float cast overflow in sqlite3VdbeMemNumerify & LOW & 2 versions & --- & 8 \\
   BC009 & Signal 6 (no stack trace) & MEDIUM & 2 versions & --- & 21 \\
   BC010 & Null ptr in sqlite3Select & HIGH & 3.31.1 & CVE-2020-9327 & 1 \\
   \midrule
   \multicolumn{5}{l}{\textbf{Total}} & \textbf{89} \\
   \bottomrule
   \end{tabular}
   \end{table}
   ```

   Case study paragraphs for notable new bugs:
   - BC001: FTS5 null pointer across ALL 4 versions. Systematic bug in FTS5 tokenizer initialization. Not version-specific — persists across 3.30.1 to 3.32.2.
   - BC004: Float cast overflow with 42 unique hashes — richest cluster. Indicates pervasive numeric edge case in `alsoAnInt()` function. Triggered by boundary float values in expressions.
   - BC006 + BC007: Null pointer pair in numeric conversion (sqlite3AtoF and sqlite3Atoi64). Related root cause in string-to-number parsing path. Both HIGH severity.
   - BC005: Window function cleanup bug (sqlite3WindowListDelete). SIGABRT during window list deallocation — indicates double-free or use-after-free in window function lifecycle.

   v3.3 on SQLite 3.53.0 paragraph: 1-hour campaign reached 30,627 edges (+17% over v3.2's 26,210). Zero crashes — all known bugs patched in latest SQLite. Demonstrates grammar reaches json.c code paths (JSON expansion was the goal of v3.3) but latest SQLite has no exploitable bugs in that module. 1-minute verification on 3.31.1 with v3.3: 12 crashes, 3 unique UBSan bugs confirmed. Grammar v3.3 remains effective on older vulnerable versions.

4. **Coverage Analysis** (~2 pages):
   - Edge count comparison across grammar versions on same SQLite target (3.31.1): v3.0 baseline → v3.2 → v3.3
   - Coverage saturation curve on 3.53.0: 50% at 10s, 90% at 20min, 95% at 37min, 99% at 50min (from checkpoint data)
   - Cross-version edge counts table for v3.2 grammar across all 4 SQLite versions
   - Include `results/charts/coverage_curves.png` figure if it exists in the results

5. **Threats to Validity** (~1 page):
   Reuse structure from old Section 4.6 but remove all bandit-specific threats. Keep:
   - Internal: stack-hash dedup heuristic (may over/under-count), coverage bitmap hash collisions, campaign duration limitations
   - External: single DBMS (SQLite), CFG cannot enforce semantic constraints, manual grammar design
   - Construct: fidelity scoring threshold arbitrary, sanitizer oracle misses logic bugs (infinite loops, incorrect query results)

- [ ] **Step 2: Verify no bandit/RL references remain**

```bash
grep -i -E "bandit|reinforcement|RL|EXP3|multi-armed|exploration.exploitation|adaptive.*sampling|uniform.*policy|uniform.*baseline|Mann-Whitney|policy.*comparison" docs/thesis/v2/chapters/c4_experiments.tex
```

Expected: no output.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c4_experiments.tex
git commit -m "docs(thesis-v2): write Chapter 4 — Experiments and Evaluation"
```

---

### Task 8: Conclusion

**Files:**
- Create: `docs/thesis/v2/chapters/conclusion.tex`

- [ ] **Step 1: Write conclusion.tex**

~2 pages. Structure:

Paragraph 1 — Summary: This thesis presented DBMS-Nautilus, a grammar-based greybox fuzzing system for automated vulnerability detection in SQLite. Built on Nautilus, the system uses a structural primitives grammar that encodes SQL patterns associated with vulnerability classes without hardcoding proof-of-concept inputs. The grammar evolved through four versions (v3.0 to v3.3, 449 to 520 rules), each refined based on evidence from coverage analysis and crash investigation.

Paragraph 2 — RQ1 answer: DBMS-Nautilus rediscovered 3 of 6 target CVEs (CVE-2020-13434, CVE-2020-9327, CVE-2020-13871) through compositional grammar generation. The grammar gap analysis revealed that 4 of 6 CVEs were unreachable until v3.2 added window functions and self-referential generated columns, demonstrating that grammar design is the dominant factor for CVE reachability.

Paragraph 3 — RQ2 answer: Beyond known CVEs, DBMS-Nautilus discovered 7 previously unreported bug classes across 89 unique crash instances spanning 4 SQLite versions. These include systematic FTS5 null pointer bugs affecting all tested versions, pervasive float cast overflow issues, and null pointer dereferences in numeric conversion functions.

Paragraph 4 — Key insight: Grammar engineering — the iterative process of analyzing coverage gaps, identifying missing structural primitives, and adding targeted production rules — is the primary driver of fuzzing effectiveness for CVE-class vulnerability discovery. The grammar defines the boundary of what the fuzzer can discover; within that boundary, coverage-guided feedback is sufficient to navigate toward bugs.

Paragraph 5 — Limitations: Single DBMS (SQLite). Context-free grammar cannot enforce semantic constraints (type correctness, referential integrity). Sanitizer oracle misses logic bugs. Manual grammar design requires CVE analysis expertise. Campaign durations of 15-30 minutes may miss bugs requiring longer exploration.

Paragraph 6 — Future work: (1) Reinforcement learning integration for adaptive rule selection — using DQN to learn which grammar rules to prioritize based on coverage and crash signals. (2) Cross-DBMS grammar portability — adapting structural primitives methodology to MySQL and PostgreSQL. (3) Semantic-aware generation — extending the context-free grammar with type constraints to generate semantically valid SQL. (4) Automated grammar expansion — using LLM-based CVE analysis to automatically extract structural patterns from vulnerability disclosures.

```latex
\chapter*{Conclusion}
\addcontentsline{toc}{chapter}{Conclusion}

% Write the full conclusion content here following the 6-paragraph structure above.
% Reference: \cite{nautilus}, \cite{sqlite}, \cite{squirrel}, \cite{sqlright}
```

- [ ] **Step 2: Commit**

```bash
git add docs/thesis/v2/chapters/conclusion.tex
git commit -m "docs(thesis-v2): write Conclusion"
```

---

### Task 9: Copy figures and verify LaTeX compilation

**Files:**
- Copy: `results/charts/*.png` → `docs/thesis/v2/figures/`

- [ ] **Step 1: Copy available chart figures**

```bash
cp results/charts/coverage_curves.png docs/thesis/v2/figures/ 2>/dev/null || true
cp results/charts/crash_accumulation.png docs/thesis/v2/figures/ 2>/dev/null || true
cp results/charts/final_comparison_dashboard.png docs/thesis/v2/figures/ 2>/dev/null || true
```

- [ ] **Step 2: Test LaTeX compilation**

```bash
cd docs/thesis/v2 && pdflatex -interaction=nonstopmode thesis.tex 2>&1 | tail -20
```

Expected: PDF generated (possibly with warnings about undefined references — those resolve after bibtex + second pass).

- [ ] **Step 3: Run BibTeX**

```bash
cd docs/thesis/v2 && bibtex thesis 2>&1 | tail -10
```

- [ ] **Step 4: Run pdflatex twice more for cross-references**

```bash
cd docs/thesis/v2 && pdflatex -interaction=nonstopmode thesis.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode thesis.tex 2>&1 | tail -5
```

- [ ] **Step 5: Verify PDF exists and check page count**

```bash
ls -la docs/thesis/v2/thesis.pdf && pdfinfo docs/thesis/v2/thesis.pdf 2>/dev/null | grep Pages || echo "pdfinfo not available"
```

Expected: thesis.pdf exists, ~40-50 pages.

- [ ] **Step 6: Fix any compilation errors**

If errors occur, fix them in the relevant `.tex` file and re-run compilation.

- [ ] **Step 7: Commit figures and build artifacts**

```bash
git add docs/thesis/v2/figures/*.png
git commit -m "docs(thesis-v2): add figures and verify compilation"
```

---

### Task 10: Final review pass — strip any remaining bandit/RL content

**Files:**
- Modify: all `docs/thesis/v2/chapters/*.tex` (if needed)

- [ ] **Step 1: Global grep for bandit/RL terms across all v2 files**

```bash
grep -r -i -n -E "bandit|reinforcement|RL agent|EXP3|multi-armed|exploration.exploitation|adaptive.*sampl|weight.*update.*policy|Thompson|uniform.*baseline|uniform.*policy" docs/thesis/v2/
```

Expected: zero matches. If any found, edit that file to remove the reference.

- [ ] **Step 2: Check all \cite{} references exist in references.bib**

```bash
grep -r -h -o '\\cite{[^}]*}' docs/thesis/v2/chapters/*.tex docs/thesis/v2/chapters/*.tex | sed 's/\\cite{//;s/}//' | tr ',' '\n' | sort -u | while read ref; do grep -q "^@.*{${ref}," docs/thesis/v2/references.bib || echo "MISSING: $ref"; done
```

Expected: no MISSING entries.

- [ ] **Step 3: Commit any fixes**

```bash
git add docs/thesis/v2/
git commit -m "docs(thesis-v2): final review pass — clean all bandit references"
```

---

## Summary

| Task | Content | Est. Size |
|------|---------|-----------|
| 1 | Scaffold + thesis.tex | ~120 lines |
| 2 | Cover + front matter (6 files) | ~200 lines |
| 3 | references.bib | ~200 lines |
| 4 | Chapter 1 — Introduction | ~200 lines (~5 pages) |
| 5 | Chapter 2 — Background | ~500 lines (~10 pages) |
| 6 | Chapter 3 — Method | ~600 lines (~15 pages) |
| 7 | Chapter 4 — Experiments | ~500 lines (~15 pages) |
| 8 | Conclusion | ~80 lines (~2 pages) |
| 9 | Figures + compilation | Build verification |
| 10 | Final review pass | Cleanup |

Total: ~2400 lines of LaTeX, ~47 pages estimated.
