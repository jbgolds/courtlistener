# Generated by Django 5.1.5 on 2025-02-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people_db", "0017_pghistory_v3_4_0_trigger_update"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="religion",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ca", "Catholic"),
                    ("pr", "Protestant"),
                    ("je", "Jewish"),
                    ("mu", "Muslim"),
                    ("at", "Atheist"),
                    ("ag", "Agnostic"),
                    ("mo", "Mormon"),
                    ("bu", "Buddhist"),
                    ("hi", "Hindu"),
                    ("ep", "Episcopalian"),
                    ("ro", "Roman Catholic"),
                    ("me", "Methodist"),
                    ("pr", "Presbyterian"),
                ],
                help_text="The religion of a person",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="personevent",
            name="religion",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ca", "Catholic"),
                    ("pr", "Protestant"),
                    ("je", "Jewish"),
                    ("mu", "Muslim"),
                    ("at", "Atheist"),
                    ("ag", "Agnostic"),
                    ("mo", "Mormon"),
                    ("bu", "Buddhist"),
                    ("hi", "Hindu"),
                    ("ep", "Episcopalian"),
                    ("ro", "Roman Catholic"),
                    ("me", "Methodist"),
                    ("pr", "Presbyterian"),
                ],
                help_text="The religion of a person",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="position_type",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Judge",
                        [
                            ("jud", "Judge"),
                            ("jus", "Justice"),
                            ("ad-law-jud", "Administrative Law Judge"),
                            ("act-jud", "Acting Judge"),
                            ("act-jus", "Acting Justice"),
                            ("act-pres-jud", "Acting Presiding Judge"),
                            (
                                "act-c-admin-jus",
                                "Acting Chief Administrative Justice",
                            ),
                            ("ass-jud", "Associate Judge"),
                            ("ass-jus", "Associate Justice"),
                            ("ass-c-jud", "Associate Chief Judge"),
                            ("ass-pres-jud", "Associate Presiding Judge"),
                            ("asst-pres-jud", "Assistant Presiding Judge"),
                            ("c-jud", "Chief Judge"),
                            ("c-jus", "Chief Justice"),
                            ("c-spec-m", "Chief Special Master"),
                            ("c-admin-jus", "Chief Administrative Justice"),
                            ("pres-jud", "Presiding Judge"),
                            ("pres-jus", "Presiding Justice"),
                            ("sup-jud", "Supervising Judge"),
                            (
                                "ad-pres-jus",
                                "Administrative Presiding Justice",
                            ),
                            ("com", "Commissioner"),
                            ("com-dep", "Deputy Commissioner"),
                            ("jud-pt", "Judge Pro Tem"),
                            ("jus-pt", "Justice Pro Tem"),
                            ("ref-jud-tr", "Judge Trial Referee"),
                            ("ref-off", "Official Referee"),
                            ("ref-state-trial", "State Trial Referee"),
                            ("ret-act-jus", "Active Retired Justice"),
                            ("ret-ass-jud", "Retired Associate Judge"),
                            ("ret-c-jud", "Retired Chief Judge"),
                            ("ret-jus", "Retired Justice"),
                            ("ret-senior-jud", "Senior Judge"),
                            ("mag", "Magistrate"),
                            ("c-mag", "Chief Magistrate"),
                            ("pres-mag", "Presiding Magistrate"),
                            ("mag-pt", "Magistrate Pro Tem"),
                            ("mag-rc", "Magistrate (Recalled)"),
                            ("mag-part-time", "Magistrate (Part-Time)"),
                            ("spec-chair", "Special Chairman"),
                            ("spec-jud", "Special Judge"),
                            ("spec-m", "Special Master"),
                            (
                                "spec-scjcbc",
                                "Special Superior Court Judge for Complex Business Cases",
                            ),
                            ("spec-tr-jud", "Special Trial Judge"),
                            ("chair", "Chairman"),
                            ("chan", "Chancellor"),
                            ("presi-jud", "President"),
                            ("res-jud", "Reserve Judge"),
                            ("trial-jud", "Trial Judge"),
                            ("vice-chan", "Vice Chancellor"),
                            ("vice-cj", "Vice Chief Judge"),
                        ],
                    ),
                    (
                        "Attorney General",
                        [
                            ("att-gen", "Attorney General"),
                            ("att-gen-ass", "Assistant Attorney General"),
                            (
                                "att-gen-ass-spec",
                                "Special Assistant Attorney General",
                            ),
                            ("sen-counsel", "Senior Counsel"),
                            ("dep-sol-gen", "Deputy Solicitor General"),
                        ],
                    ),
                    (
                        "Appointing Authority",
                        [
                            ("pres", "President of the United States"),
                            ("gov", "Governor"),
                            ("mayor", "Mayor"),
                        ],
                    ),
                    (
                        "Clerkships",
                        [
                            ("clerk", "Clerk"),
                            ("clerk-chief-dep", "Chief Deputy Clerk"),
                            ("staff-atty", "Staff Attorney"),
                        ],
                    ),
                    ("prof", "Professor"),
                    ("adj-prof", "Adjunct Professor"),
                    ("prac", "Practitioner"),
                    ("pros", "Prosecutor"),
                    ("pub-def", "Public Defender"),
                    ("da", "District Attorney"),
                    ("ada", "Assistant District Attorney"),
                    ("legis", "Legislator"),
                    ("sen", "Senator"),
                    ("state-sen", "State Senator"),
                ],
                help_text="If this is a judicial position, this indicates the role the person had. This field may be blank if job_title is complete instead.",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="positionevent",
            name="position_type",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Judge",
                        [
                            ("jud", "Judge"),
                            ("jus", "Justice"),
                            ("ad-law-jud", "Administrative Law Judge"),
                            ("act-jud", "Acting Judge"),
                            ("act-jus", "Acting Justice"),
                            ("act-pres-jud", "Acting Presiding Judge"),
                            (
                                "act-c-admin-jus",
                                "Acting Chief Administrative Justice",
                            ),
                            ("ass-jud", "Associate Judge"),
                            ("ass-jus", "Associate Justice"),
                            ("ass-c-jud", "Associate Chief Judge"),
                            ("ass-pres-jud", "Associate Presiding Judge"),
                            ("asst-pres-jud", "Assistant Presiding Judge"),
                            ("c-jud", "Chief Judge"),
                            ("c-jus", "Chief Justice"),
                            ("c-spec-m", "Chief Special Master"),
                            ("c-admin-jus", "Chief Administrative Justice"),
                            ("pres-jud", "Presiding Judge"),
                            ("pres-jus", "Presiding Justice"),
                            ("sup-jud", "Supervising Judge"),
                            (
                                "ad-pres-jus",
                                "Administrative Presiding Justice",
                            ),
                            ("com", "Commissioner"),
                            ("com-dep", "Deputy Commissioner"),
                            ("jud-pt", "Judge Pro Tem"),
                            ("jus-pt", "Justice Pro Tem"),
                            ("ref-jud-tr", "Judge Trial Referee"),
                            ("ref-off", "Official Referee"),
                            ("ref-state-trial", "State Trial Referee"),
                            ("ret-act-jus", "Active Retired Justice"),
                            ("ret-ass-jud", "Retired Associate Judge"),
                            ("ret-c-jud", "Retired Chief Judge"),
                            ("ret-jus", "Retired Justice"),
                            ("ret-senior-jud", "Senior Judge"),
                            ("mag", "Magistrate"),
                            ("c-mag", "Chief Magistrate"),
                            ("pres-mag", "Presiding Magistrate"),
                            ("mag-pt", "Magistrate Pro Tem"),
                            ("mag-rc", "Magistrate (Recalled)"),
                            ("mag-part-time", "Magistrate (Part-Time)"),
                            ("spec-chair", "Special Chairman"),
                            ("spec-jud", "Special Judge"),
                            ("spec-m", "Special Master"),
                            (
                                "spec-scjcbc",
                                "Special Superior Court Judge for Complex Business Cases",
                            ),
                            ("spec-tr-jud", "Special Trial Judge"),
                            ("chair", "Chairman"),
                            ("chan", "Chancellor"),
                            ("presi-jud", "President"),
                            ("res-jud", "Reserve Judge"),
                            ("trial-jud", "Trial Judge"),
                            ("vice-chan", "Vice Chancellor"),
                            ("vice-cj", "Vice Chief Judge"),
                        ],
                    ),
                    (
                        "Attorney General",
                        [
                            ("att-gen", "Attorney General"),
                            ("att-gen-ass", "Assistant Attorney General"),
                            (
                                "att-gen-ass-spec",
                                "Special Assistant Attorney General",
                            ),
                            ("sen-counsel", "Senior Counsel"),
                            ("dep-sol-gen", "Deputy Solicitor General"),
                        ],
                    ),
                    (
                        "Appointing Authority",
                        [
                            ("pres", "President of the United States"),
                            ("gov", "Governor"),
                            ("mayor", "Mayor"),
                        ],
                    ),
                    (
                        "Clerkships",
                        [
                            ("clerk", "Clerk"),
                            ("clerk-chief-dep", "Chief Deputy Clerk"),
                            ("staff-atty", "Staff Attorney"),
                        ],
                    ),
                    ("prof", "Professor"),
                    ("adj-prof", "Adjunct Professor"),
                    ("prac", "Practitioner"),
                    ("pros", "Prosecutor"),
                    ("pub-def", "Public Defender"),
                    ("da", "District Attorney"),
                    ("ada", "Assistant District Attorney"),
                    ("legis", "Legislator"),
                    ("sen", "Senator"),
                    ("state-sen", "State Senator"),
                ],
                help_text="If this is a judicial position, this indicates the role the person had. This field may be blank if job_title is complete instead.",
                max_length=20,
                null=True,
            ),
        ),
    ]
