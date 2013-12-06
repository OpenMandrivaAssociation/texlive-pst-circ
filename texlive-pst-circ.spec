# revision 31820
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-circ
# catalog-date 2013-10-03 14:41:14 +0200
# catalog-license lppl
# catalog-version 2.05
Name:		texlive-pst-circ
Version:	2.05
Release:	5
Summary:	PSTricks package for drawing electric circuits
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-circ
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-circ.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-circ.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is built using PSTricks and in particular pst-node.
It can easily draw current 2-terminal devices and some 3- and
4-terminal devices used in electronic or electric theory. The
package's macros are designed with a view to 'logical'
representation of circuits, as far as possible, so as to
relieve the user of purely graphical considerations when
expressing a circuit.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-circ/pst-circ.pro
%{_texmfdistdir}/tex/generic/pst-circ/pst-circ.tex
%{_texmfdistdir}/tex/latex/pst-circ/pst-circ.sty
%doc %{_texmfdistdir}/doc/generic/pst-circ/Changes
%doc %{_texmfdistdir}/doc/generic/pst-circ/README
%doc %{_texmfdistdir}/doc/generic/pst-circ/dtk03-3.bib
%doc %{_texmfdistdir}/doc/generic/pst-circ/dtk03-3.ltx
%doc %{_texmfdistdir}/doc/generic/pst-circ/dtk03-3.pdf
%doc %{_texmfdistdir}/doc/generic/pst-circ/dtk03-3.tex
%doc %{_texmfdistdir}/doc/generic/pst-circ/pst-circ-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-circ/pst-circ-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-circ/pst-circ-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
