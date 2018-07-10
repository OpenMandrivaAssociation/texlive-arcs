# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/arcs
# catalog-date 2006-10-12 15:06:10 +0200
# catalog-license lppl
# catalog-version 1
Name:		texlive-arcs
Version:	1
Release:	2
Summary:	Draw arcs over and under text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arcs
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arcs.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2-2
+ Revision: 749344
- Rebuild to reduce used resources

* Sat Nov 12 2011 Paulo Andrade <pcpa@mandriva.com.br> 2-1
+ Revision: 730214
- texlive-arcs

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1-1
+ Revision: 717851
- texlive-arcs
- texlive-arcs
- texlive-arcs
- texlive-arcs
- texlive-arcs

