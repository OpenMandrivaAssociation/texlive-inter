%global tl_name inter
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The inter font face with support for LaTeX, XeLaTeX, and LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/inter
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Inter Sans family of fonts (version 3.015), designed by Rasmus
Andersson. Inter is a typeface specially designed for user interfaces
with focus on high legibility of small-to-medium sized text on computer
screens. The family features a tall x-height to aid in readability of
mixed-case and lower-case text.

