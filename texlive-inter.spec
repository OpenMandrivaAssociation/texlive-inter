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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Inter Sans family of fonts (version 3.015), designed by Rasmus
Andersson. Inter is a typeface specially designed for user interfaces
with focus on high legibility of small-to-medium sized text on computer
screens. The family features a tall x-height to aid in readability of
mixed-case and lower-case text.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from inter:
Map Inter.map
TL_DROPIN_EOF
