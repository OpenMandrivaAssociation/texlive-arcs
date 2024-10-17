Name:		texlive-arcs
Version:	15878
Release:	2
Summary:	Draw arcs over and under text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arcs
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides two commands for placing an arc over
(\overarc) or under (\underarc) a piece of text. (The text may
be up to three letters long.) The commands generate an \hbox,
and may be used both in text and in maths formulae.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/arcs/arcs.sty
%doc %{_texmfdistdir}/doc/latex/arcs/README
%doc %{_texmfdistdir}/doc/latex/arcs/arcs.pdf
%doc %{_texmfdistdir}/doc/latex/arcs/arcstest.tex
#- source
%doc %{_texmfdistdir}/source/latex/arcs/arcs.dtx
%doc %{_texmfdistdir}/source/latex/arcs/arcs.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
