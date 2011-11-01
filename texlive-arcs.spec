Name:		texlive-arcs
Version:	1
Release:	1
Summary:	Draw arcs over and under text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arcs
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides two commands for placing an arc over
(\overarc) or under (\underarc) a piece of text. (The text may
be up to three letters long.) The commands generate an \hbox,
and may be used both in text and in maths formulae.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
