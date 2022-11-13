Name:		texlive-pst-circ
Version:	60464
Release:	1
Summary:	PSTricks package for drawing electric circuits
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-circ
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-circ.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-circ.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/dvips/pst-circ
%{_texmfdistdir}/tex/generic/pst-circ
%{_texmfdistdir}/tex/latex/pst-circ
%doc %{_texmfdistdir}/doc/generic/pst-circ

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
