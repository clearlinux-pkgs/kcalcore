#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcalcore
Version  : 18.12.3
Release  : 6
URL      : https://download.kde.org/stable/applications/18.12.3/src/kcalcore-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/kcalcore-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/kcalcore-18.12.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0
Requires: kcalcore-data = %{version}-%{release}
Requires: kcalcore-lib = %{version}-%{release}
Requires: kcalcore-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : pkg-config
BuildRequires : pkgconfig(libical)
BuildRequires : qtbase-dev mesa-dev

%description
To build these tests, build with the cmake option KDE4_BUILD_TESTS=ON.
To run all these tests, enter the command 'ctest'.
Details of failed tests are output to FAILED.log, and in the case of recurrence tests,
to the .out files equivalent to the .ref files containing the expected results.

%package data
Summary: data components for the kcalcore package.
Group: Data

%description data
data components for the kcalcore package.


%package dev
Summary: dev components for the kcalcore package.
Group: Development
Requires: kcalcore-lib = %{version}-%{release}
Requires: kcalcore-data = %{version}-%{release}
Provides: kcalcore-devel = %{version}-%{release}

%description dev
dev components for the kcalcore package.


%package lib
Summary: lib components for the kcalcore package.
Group: Libraries
Requires: kcalcore-data = %{version}-%{release}
Requires: kcalcore-license = %{version}-%{release}

%description lib
lib components for the kcalcore package.


%package license
Summary: license components for the kcalcore package.
Group: Default

%description license
license components for the kcalcore package.


%prep
%setup -q -n kcalcore-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551994323
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1551994323
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcalcore
cp COPYING %{buildroot}/usr/share/package-licenses/kcalcore/COPYING
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kcalcore/cmake_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/kcalcore.categories
/usr/share/xdg/kcalcore.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KCalCore/KCalCore/Alarm
/usr/include/KF5/KCalCore/KCalCore/Attachment
/usr/include/KF5/KCalCore/KCalCore/Attendee
/usr/include/KF5/KCalCore/KCalCore/CalFilter
/usr/include/KF5/KCalCore/KCalCore/CalFormat
/usr/include/KF5/KCalCore/KCalCore/CalStorage
/usr/include/KF5/KCalCore/KCalCore/Calendar
/usr/include/KF5/KCalCore/KCalCore/CustomProperties
/usr/include/KF5/KCalCore/KCalCore/Duration
/usr/include/KF5/KCalCore/KCalCore/Event
/usr/include/KF5/KCalCore/KCalCore/Exceptions
/usr/include/KF5/KCalCore/KCalCore/FileStorage
/usr/include/KF5/KCalCore/KCalCore/FreeBusy
/usr/include/KF5/KCalCore/KCalCore/FreeBusyCache
/usr/include/KF5/KCalCore/KCalCore/FreeBusyPeriod
/usr/include/KF5/KCalCore/KCalCore/ICalFormat
/usr/include/KF5/KCalCore/KCalCore/Incidence
/usr/include/KF5/KCalCore/KCalCore/IncidenceBase
/usr/include/KF5/KCalCore/KCalCore/Journal
/usr/include/KF5/KCalCore/KCalCore/MemoryCalendar
/usr/include/KF5/KCalCore/KCalCore/OccurrenceIterator
/usr/include/KF5/KCalCore/KCalCore/Period
/usr/include/KF5/KCalCore/KCalCore/Person
/usr/include/KF5/KCalCore/KCalCore/Recurrence
/usr/include/KF5/KCalCore/KCalCore/RecurrenceRule
/usr/include/KF5/KCalCore/KCalCore/ScheduleMessage
/usr/include/KF5/KCalCore/KCalCore/SortableList
/usr/include/KF5/KCalCore/KCalCore/Sorting
/usr/include/KF5/KCalCore/KCalCore/Todo
/usr/include/KF5/KCalCore/KCalCore/VCalFormat
/usr/include/KF5/KCalCore/KCalCore/Visitor
/usr/include/KF5/KCalCore/kcalcore/alarm.h
/usr/include/KF5/KCalCore/kcalcore/attachment.h
/usr/include/KF5/KCalCore/kcalcore/attendee.h
/usr/include/KF5/KCalCore/kcalcore/calendar.h
/usr/include/KF5/KCalCore/kcalcore/calfilter.h
/usr/include/KF5/KCalCore/kcalcore/calformat.h
/usr/include/KF5/KCalCore/kcalcore/calstorage.h
/usr/include/KF5/KCalCore/kcalcore/customproperties.h
/usr/include/KF5/KCalCore/kcalcore/duration.h
/usr/include/KF5/KCalCore/kcalcore/event.h
/usr/include/KF5/KCalCore/kcalcore/exceptions.h
/usr/include/KF5/KCalCore/kcalcore/filestorage.h
/usr/include/KF5/KCalCore/kcalcore/freebusy.h
/usr/include/KF5/KCalCore/kcalcore/freebusycache.h
/usr/include/KF5/KCalCore/kcalcore/freebusyperiod.h
/usr/include/KF5/KCalCore/kcalcore/icalformat.h
/usr/include/KF5/KCalCore/kcalcore/incidence.h
/usr/include/KF5/KCalCore/kcalcore/incidencebase.h
/usr/include/KF5/KCalCore/kcalcore/journal.h
/usr/include/KF5/KCalCore/kcalcore/kcalcore_export.h
/usr/include/KF5/KCalCore/kcalcore/memorycalendar.h
/usr/include/KF5/KCalCore/kcalcore/occurrenceiterator.h
/usr/include/KF5/KCalCore/kcalcore/period.h
/usr/include/KF5/KCalCore/kcalcore/person.h
/usr/include/KF5/KCalCore/kcalcore/recurrence.h
/usr/include/KF5/KCalCore/kcalcore/recurrencerule.h
/usr/include/KF5/KCalCore/kcalcore/schedulemessage.h
/usr/include/KF5/KCalCore/kcalcore/sortablelist.h
/usr/include/KF5/KCalCore/kcalcore/sorting.h
/usr/include/KF5/KCalCore/kcalcore/supertrait.h
/usr/include/KF5/KCalCore/kcalcore/todo.h
/usr/include/KF5/KCalCore/kcalcore/vcalformat.h
/usr/include/KF5/KCalCore/kcalcore/visitor.h
/usr/include/KF5/kcalcore_version.h
/usr/lib64/cmake/KF5CalendarCore/FindLibIcal.cmake
/usr/lib64/cmake/KF5CalendarCore/KF5CalendarCoreConfig.cmake
/usr/lib64/cmake/KF5CalendarCore/KF5CalendarCoreConfigVersion.cmake
/usr/lib64/cmake/KF5CalendarCore/KF5CalendarCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5CalendarCore/KF5CalendarCoreTargets.cmake
/usr/lib64/libKF5CalendarCore.so
/usr/lib64/qt5/mkspecs/modules/qt_KCalCore.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5CalendarCore.so.5
/usr/lib64/libKF5CalendarCore.so.5.10.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalcore/COPYING
/usr/share/package-licenses/kcalcore/cmake_COPYING-CMAKE-SCRIPTS
