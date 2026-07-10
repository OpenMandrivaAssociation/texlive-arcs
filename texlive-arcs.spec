%global tl_name arcs
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	Draw arcs over and under text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arcs
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides two commands for placing an arc over (\overarc) or
under (\underarc) a piece of text. (The text may be up to three letters
long.) The commands generate an \hbox, and may be used both in text and
in maths formulae.

