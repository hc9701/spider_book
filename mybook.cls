% -- coding: UTF-8 --
\LoadClass{book}
\usepackage{xcolor}
\usepackage{framed}
\usepackage[colorlinks,linkcolor=black]{hyperref}

\renewcommand{\contentsname}{目录}
\renewcommand{\thefootnote}{[\arabic{footnote}]}
\renewcommand{\figurename}{图}
\renewcommand{\tablename}{表}


\def\equationautorefname{式}%
\def\footnoteautorefname{脚注}%
\def\itemautorefname{项}%
\def\figureautorefname{图}%
\def\tableautorefname{表}%
\def\partautorefname{篇}%
\def\appendixautorefname{附录}%
\def\chapterautorefname{章}%
\def\sectionautorefname{节}%
\def\subsectionautorefname{小小节}%
\def\subsubsectionautorefname{subsubsection}%
\def\paragraphautorefname{段落}%
\def\subparagraphautorefname{子段落}%
\def\FancyVerbLineautorefname{行}%
\def\theoremautorefname{定理}%

\newcommand{\beforecontent}[2]{
  \colorlet{shadecolor}{blue!20}
  \begin{shaded}
    #1
    \begin{flushright}
      ——#2
    \end{flushright}
  \end{shaded}
}
\newcommand{\aftercontent}[1]{
  \colorlet{shadecolor}{gray!15}
  \begin{shaded}
    \textbf{本章小结}

    #1
  \end{shaded}
}
\newcommand{\note}[1]{
  \colorlet{shadecolor}{orange!20}
  \begin{shaded}
    \textbf{友情提醒}

    #1
  \end{shaded}
}
\newcommand{\code}[1]{
  \begin{center}
    代码清单 #1
  \end{center}
}
\newcommand{\tip}[1]{
  \colorlet{shadecolor}{orange!10}
  \begin{shaded}
    \textbf{小诀窍}

    #1
  \end{shaded}
}
