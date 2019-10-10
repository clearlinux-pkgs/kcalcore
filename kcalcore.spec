#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcalcore
Version  : 19.08.2
Release  : 15
URL      : https://download.kde.org/stable/applications/19.08.2/src/kcalcore-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/kcalcore-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/kcalcore-19.08.2.tar.xz.sig
Summary  : The KDE calendar access library
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
Requires: kcalcore = %{version}-%{release}
Requires: kcalcore = %{version}-%{release}

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
%setup -q -n kcalcore-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570738936
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570738936
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
/usr/share/qlogging-categories5/kcalendarcore.categories
/usr/share/qlogging-categories5/kcalendarcore.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KCalendarCore/KCalCore/Alarm
/usr/include/KF5/KCalendarCore/KCalCore/Attachment
/usr/include/KF5/KCalendarCore/KCalCore/Attendee
/usr/include/KF5/KCalendarCore/KCalCore/CalFilter
/usr/include/KF5/KCalendarCore/KCalCore/CalFormat
/usr/include/KF5/KCalendarCore/KCalCore/CalStorage
/usr/include/KF5/KCalendarCore/KCalCore/Calendar
/usr/include/KF5/KCalendarCore/KCalCore/CustomProperties
/usr/include/KF5/KCalendarCore/KCalCore/Duration
/usr/include/KF5/KCalendarCore/KCalCore/Event
/usr/include/KF5/KCalendarCore/KCalCore/Exceptions
/usr/include/KF5/KCalendarCore/KCalCore/FileStorage
/usr/include/KF5/KCalendarCore/KCalCore/FreeBusy
/usr/include/KF5/KCalendarCore/KCalCore/FreeBusyCache
/usr/include/KF5/KCalendarCore/KCalCore/FreeBusyPeriod
/usr/include/KF5/KCalendarCore/KCalCore/ICalFormat
/usr/include/KF5/KCalendarCore/KCalCore/Incidence
/usr/include/KF5/KCalendarCore/KCalCore/IncidenceBase
/usr/include/KF5/KCalendarCore/KCalCore/Journal
/usr/include/KF5/KCalendarCore/KCalCore/MemoryCalendar
/usr/include/KF5/KCalendarCore/KCalCore/OccurrenceIterator
/usr/include/KF5/KCalendarCore/KCalCore/Period
/usr/include/KF5/KCalendarCore/KCalCore/Person
/usr/include/KF5/KCalendarCore/KCalCore/Recurrence
/usr/include/KF5/KCalendarCore/KCalCore/RecurrenceRule
/usr/include/KF5/KCalendarCore/KCalCore/ScheduleMessage
/usr/include/KF5/KCalendarCore/KCalCore/Sorting
/usr/include/KF5/KCalendarCore/KCalCore/Todo
/usr/include/KF5/KCalendarCore/KCalCore/VCalFormat
/usr/include/KF5/KCalendarCore/KCalCore/Visitor
/usr/include/KF5/KCalendarCore/KCalendarCore/Alarm
/usr/include/KF5/KCalendarCore/KCalendarCore/Attachment
/usr/include/KF5/KCalendarCore/KCalendarCore/Attendee
/usr/include/KF5/KCalendarCore/KCalendarCore/CalFilter
/usr/include/KF5/KCalendarCore/KCalendarCore/CalFormat
/usr/include/KF5/KCalendarCore/KCalendarCore/CalStorage
/usr/include/KF5/KCalendarCore/KCalendarCore/Calendar
/usr/include/KF5/KCalendarCore/KCalendarCore/CustomProperties
/usr/include/KF5/KCalendarCore/KCalendarCore/Duration
/usr/include/KF5/KCalendarCore/KCalendarCore/Event
/usr/include/KF5/KCalendarCore/KCalendarCore/Exceptions
/usr/include/KF5/KCalendarCore/KCalendarCore/FileStorage
/usr/include/KF5/KCalendarCore/KCalendarCore/FreeBusy
/usr/include/KF5/KCalendarCore/KCalendarCore/FreeBusyCache
/usr/include/KF5/KCalendarCore/KCalendarCore/FreeBusyPeriod
/usr/include/KF5/KCalendarCore/KCalendarCore/ICalFormat
/usr/include/KF5/KCalendarCore/KCalendarCore/Incidence
/usr/include/KF5/KCalendarCore/KCalendarCore/IncidenceBase
/usr/include/KF5/KCalendarCore/KCalendarCore/Journal
/usr/include/KF5/KCalendarCore/KCalendarCore/MemoryCalendar
/usr/include/KF5/KCalendarCore/KCalendarCore/OccurrenceIterator
/usr/include/KF5/KCalendarCore/KCalendarCore/Period
/usr/include/KF5/KCalendarCore/KCalendarCore/Person
/usr/include/KF5/KCalendarCore/KCalendarCore/Recurrence
/usr/include/KF5/KCalendarCore/KCalendarCore/RecurrenceRule
/usr/include/KF5/KCalendarCore/KCalendarCore/ScheduleMessage
/usr/include/KF5/KCalendarCore/KCalendarCore/Sorting
/usr/include/KF5/KCalendarCore/KCalendarCore/Todo
/usr/include/KF5/KCalendarCore/KCalendarCore/VCalFormat
/usr/include/KF5/KCalendarCore/KCalendarCore/Visitor
/usr/include/KF5/KCalendarCore/kcalcore/alarm.h
/usr/include/KF5/KCalendarCore/kcalcore/attachment.h
/usr/include/KF5/KCalendarCore/kcalcore/attendee.h
/usr/include/KF5/KCalendarCore/kcalcore/calendar.h
/usr/include/KF5/KCalendarCore/kcalcore/calfilter.h
/usr/include/KF5/KCalendarCore/kcalcore/calformat.h
/usr/include/KF5/KCalendarCore/kcalcore/calstorage.h
/usr/include/KF5/KCalendarCore/kcalcore/customproperties.h
/usr/include/KF5/KCalendarCore/kcalcore/duration.h
/usr/include/KF5/KCalendarCore/kcalcore/event.h
/usr/include/KF5/KCalendarCore/kcalcore/exceptions.h
/usr/include/KF5/KCalendarCore/kcalcore/filestorage.h
/usr/include/KF5/KCalendarCore/kcalcore/freebusy.h
/usr/include/KF5/KCalendarCore/kcalcore/freebusycache.h
/usr/include/KF5/KCalendarCore/kcalcore/freebusyperiod.h
/usr/include/KF5/KCalendarCore/kcalcore/icalformat.h
/usr/include/KF5/KCalendarCore/kcalcore/incidence.h
/usr/include/KF5/KCalendarCore/kcalcore/incidencebase.h
/usr/include/KF5/KCalendarCore/kcalcore/journal.h
/usr/include/KF5/KCalendarCore/kcalcore/kcalendarcore_export.h
/usr/include/KF5/KCalendarCore/kcalcore/memorycalendar.h
/usr/include/KF5/KCalendarCore/kcalcore/occurrenceiterator.h
/usr/include/KF5/KCalendarCore/kcalcore/period.h
/usr/include/KF5/KCalendarCore/kcalcore/person.h
/usr/include/KF5/KCalendarCore/kcalcore/recurrence.h
/usr/include/KF5/KCalendarCore/kcalcore/recurrencerule.h
/usr/include/KF5/KCalendarCore/kcalcore/schedulemessage.h
/usr/include/KF5/KCalendarCore/kcalcore/sorting.h
/usr/include/KF5/KCalendarCore/kcalcore/todo.h
/usr/include/KF5/KCalendarCore/kcalcore/vcalformat.h
/usr/include/KF5/KCalendarCore/kcalcore/visitor.h
/usr/include/KF5/KCalendarCore/kcalendarcore/alarm.h
/usr/include/KF5/KCalendarCore/kcalendarcore/attachment.h
/usr/include/KF5/KCalendarCore/kcalendarcore/attendee.h
/usr/include/KF5/KCalendarCore/kcalendarcore/calendar.h
/usr/include/KF5/KCalendarCore/kcalendarcore/calfilter.h
/usr/include/KF5/KCalendarCore/kcalendarcore/calformat.h
/usr/include/KF5/KCalendarCore/kcalendarcore/calstorage.h
/usr/include/KF5/KCalendarCore/kcalendarcore/customproperties.h
/usr/include/KF5/KCalendarCore/kcalendarcore/duration.h
/usr/include/KF5/KCalendarCore/kcalendarcore/event.h
/usr/include/KF5/KCalendarCore/kcalendarcore/exceptions.h
/usr/include/KF5/KCalendarCore/kcalendarcore/filestorage.h
/usr/include/KF5/KCalendarCore/kcalendarcore/freebusy.h
/usr/include/KF5/KCalendarCore/kcalendarcore/freebusycache.h
/usr/include/KF5/KCalendarCore/kcalendarcore/freebusyperiod.h
/usr/include/KF5/KCalendarCore/kcalendarcore/icalformat.h
/usr/include/KF5/KCalendarCore/kcalendarcore/incidence.h
/usr/include/KF5/KCalendarCore/kcalendarcore/incidencebase.h
/usr/include/KF5/KCalendarCore/kcalendarcore/journal.h
/usr/include/KF5/KCalendarCore/kcalendarcore/kcalendarcore_export.h
/usr/include/KF5/KCalendarCore/kcalendarcore/memorycalendar.h
/usr/include/KF5/KCalendarCore/kcalendarcore/occurrenceiterator.h
/usr/include/KF5/KCalendarCore/kcalendarcore/period.h
/usr/include/KF5/KCalendarCore/kcalendarcore/person.h
/usr/include/KF5/KCalendarCore/kcalendarcore/recurrence.h
/usr/include/KF5/KCalendarCore/kcalendarcore/recurrencerule.h
/usr/include/KF5/KCalendarCore/kcalendarcore/schedulemessage.h
/usr/include/KF5/KCalendarCore/kcalendarcore/sorting.h
/usr/include/KF5/KCalendarCore/kcalendarcore/todo.h
/usr/include/KF5/KCalendarCore/kcalendarcore/vcalformat.h
/usr/include/KF5/KCalendarCore/kcalendarcore/visitor.h
/usr/include/KF5/kcalcore_version.h
/usr/include/KF5/kcalendarcore_version.h
/usr/lib64/cmake/KF5CalendarCore/FindLibIcal.cmake
/usr/lib64/cmake/KF5CalendarCore/KF5CalendarCoreConfig.cmake
/usr/lib64/cmake/KF5CalendarCore/KF5CalendarCoreConfigVersion.cmake
/usr/lib64/cmake/KF5CalendarCore/KF5CalendarCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5CalendarCore/KF5CalendarCoreTargets.cmake
/usr/lib64/libKF5CalendarCore.so
/usr/lib64/qt5/mkspecs/modules/qt_KCalendarCore.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5CalendarCore.so.5
/usr/lib64/libKF5CalendarCore.so.5.12.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalcore/COPYING
/usr/share/package-licenses/kcalcore/cmake_COPYING-CMAKE-SCRIPTS
