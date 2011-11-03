# revision 22444
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-circ
# catalog-date 2011-05-12 00:58:47 +0200
# catalog-license lppl
# catalog-version 2.02
Name:		texlive-pst-circ
Version:	2.02
Release:	1
Summary:	PSTricks package for drawing electric circuits
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-circ
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-circ.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-circ.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-circ.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Pst-circ is a package built using PSTricks and in particular
pst-node. It can easily draw current 2-terminal devices and
some 3- and 4-terminal devices used in electronic or electric
theory. The package's macros are designed with a view to
'logical' representation of circuits, as far as possible, so as
to relieve the user of purely graphical considerations when
expressing a circuit.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-circ/pst-circ.pro
%{_texmfdistdir}/tex/generic/pst-circ/pst-circ.tex
%{_texmfdistdir}/tex/latex/pst-circ/pst-circ.sty
%doc %{_texmfdistdir}/doc/generic/pst-circ/Changes
%doc %{_texmfdistdir}/doc/generic/pst-circ/README
%doc %{_texmfdistdir}/doc/generic/pst-circ/more_docs/dtk03-3.pdf
%doc %{_texmfdistdir}/doc/generic/pst-circ/pst-circ-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-circ/pst-circ-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-circ/pst-circ-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-circ/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
