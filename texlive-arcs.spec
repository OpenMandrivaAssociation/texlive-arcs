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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides two commands for placing an arc over (\overarc) or
under (\underarc) a piece of text. (The text may be up to three letters
long.) The commands generate an \hbox, and may be used both in text and
in maths formulae.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/arcs
%dir %{_datadir}/texmf-dist/source/latex/arcs
%dir %{_datadir}/texmf-dist/tex/latex/arcs
%doc %{_datadir}/texmf-dist/doc/latex/arcs/README
%doc %{_datadir}/texmf-dist/doc/latex/arcs/arcs.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arcs/arcstest.tex
%doc %{_datadir}/texmf-dist/source/latex/arcs/arcs.dtx
%doc %{_datadir}/texmf-dist/source/latex/arcs/arcs.ins
%{_datadir}/texmf-dist/tex/latex/arcs/arcs.sty
