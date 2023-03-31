Name:		texlive-inter
Version:	58892
Release:	2
Summary:	The inter font face with support for LaTeX, XeLaTeX, and LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/inter
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Inter Sans family of fonts (version 3.015),
designed by Rasmus Andersson. Inter is a typeface specially
designed for user interfaces with focus on high legibility of
small-to-medium sized text on computer screens. The family
features a tall x-height to aid in readability of mixed-case
and lower-case text.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/inter
%{_texmfdistdir}/fonts/vf/public/inter
%{_texmfdistdir}/fonts/type1/public/inter
%{_texmfdistdir}/fonts/tfm/public/inter
%{_texmfdistdir}/fonts/opentype/public/inter
%{_texmfdistdir}/fonts/map/dvips/inter
%{_texmfdistdir}/fonts/enc/dvips/inter
%doc %{_texmfdistdir}/doc/fonts/inter

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
