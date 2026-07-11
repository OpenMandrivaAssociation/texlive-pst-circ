%global tl_name pst-circ
%global tl_revision 72519

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.20
Release:	%{tl_revision}.1
Summary:	PSTricks package for drawing electric circuits
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-circ
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-circ.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-circ.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is built using PSTricks and in particular pst-node. It can
easily draw current 2-terminal devices and some 3- and 4-terminal
devices used in electronic or electric theory. The package's macros are
designed with a view to 'logical' representation of circuits, as far as
possible, so as to relieve the user of purely graphical considerations
when expressing a circuit.

