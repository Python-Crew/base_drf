# Generated by Django 3.1 on 2021-12-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0004_auto_20211223_1204"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="price_net_amount",
            new_name="price_amount",
        ),
        migrations.RemoveField(
            model_name="order",
            name="amount",
        ),
        migrations.AlterField(
            model_name="order",
            name="currency",
            field=models.CharField(
                choices=[
                    ("LUF", "LUF"),
                    ("HUF", "HUF"),
                    ("FIM", "FIM"),
                    ("DZD", "DZD"),
                    ("GQE", "GQE"),
                    ("TRY", "TRY"),
                    ("YDD", "YDD"),
                    ("EEK", "EEK"),
                    ("HRK", "HRK"),
                    ("ZAL", "ZAL"),
                    ("CNH", "CNH"),
                    ("KGS", "KGS"),
                    ("UYP", "UYP"),
                    ("STN", "STN"),
                    ("BEF", "BEF"),
                    ("ARA", "ARA"),
                    ("UGS", "UGS"),
                    ("BOB", "BOB"),
                    ("IDR", "IDR"),
                    ("ECV", "ECV"),
                    ("XPF", "XPF"),
                    ("TTD", "TTD"),
                    ("USS", "USS"),
                    ("XUA", "XUA"),
                    ("KWD", "KWD"),
                    ("BAD", "BAD"),
                    ("MWK", "MWK"),
                    ("BYR", "BYR"),
                    ("MZN", "MZN"),
                    ("RUR", "RUR"),
                    ("TPE", "TPE"),
                    ("HNL", "HNL"),
                    ("TZS", "TZS"),
                    ("XPT", "XPT"),
                    ("IRR", "IRR"),
                    ("LSL", "LSL"),
                    ("GNS", "GNS"),
                    ("JMD", "JMD"),
                    ("BTN", "BTN"),
                    ("CUC", "CUC"),
                    ("ISJ", "ISJ"),
                    ("PYG", "PYG"),
                    ("KYD", "KYD"),
                    ("QAR", "QAR"),
                    ("TJS", "TJS"),
                    ("LKR", "LKR"),
                    ("CZK", "CZK"),
                    ("GEL", "GEL"),
                    ("HTG", "HTG"),
                    ("CUP", "CUP"),
                    ("BWP", "BWP"),
                    ("MYR", "MYR"),
                    ("ARS", "ARS"),
                    ("AFN", "AFN"),
                    ("AON", "AON"),
                    ("YER", "YER"),
                    ("ARM", "ARM"),
                    ("PLN", "PLN"),
                    ("USN", "USN"),
                    ("XDR", "XDR"),
                    ("GIP", "GIP"),
                    ("RWF", "RWF"),
                    ("MAD", "MAD"),
                    ("MXP", "MXP"),
                    ("ARP", "ARP"),
                    ("OMR", "OMR"),
                    ("XAG", "XAG"),
                    ("TMM", "TMM"),
                    ("XBD", "XBD"),
                    ("UYI", "UYI"),
                    ("BOV", "BOV"),
                    ("MTP", "MTP"),
                    ("CNX", "CNX"),
                    ("BGO", "BGO"),
                    ("PEN", "PEN"),
                    ("IEP", "IEP"),
                    ("ITL", "ITL"),
                    ("SUR", "SUR"),
                    ("ILS", "ILS"),
                    ("TND", "TND"),
                    ("AZM", "AZM"),
                    ("ZWR", "ZWR"),
                    ("BYB", "BYB"),
                    ("GHC", "GHC"),
                    ("MXN", "MXN"),
                    ("TJR", "TJR"),
                    ("XBA", "XBA"),
                    ("CVE", "CVE"),
                    ("SRD", "SRD"),
                    ("SRG", "SRG"),
                    ("VEF", "VEF"),
                    ("CAD", "CAD"),
                    ("BAN", "BAN"),
                    ("UZS", "UZS"),
                    ("ZRZ", "ZRZ"),
                    ("LRD", "LRD"),
                    ("XFU", "XFU"),
                    ("BRN", "BRN"),
                    ("XBB", "XBB"),
                    ("BZD", "BZD"),
                    ("ESB", "ESB"),
                    ("ERN", "ERN"),
                    ("BGM", "BGM"),
                    ("STD", "STD"),
                    ("ZMK", "ZMK"),
                    ("DOP", "DOP"),
                    ("TOP", "TOP"),
                    ("WST", "WST"),
                    ("XEU", "XEU"),
                    ("ECS", "ECS"),
                    ("YUD", "YUD"),
                    ("FRF", "FRF"),
                    ("ADP", "ADP"),
                    ("TWD", "TWD"),
                    ("BRR", "BRR"),
                    ("KMF", "KMF"),
                    ("DKK", "DKK"),
                    ("SGD", "SGD"),
                    ("SKK", "SKK"),
                    ("VEB", "VEB"),
                    ("SLL", "SLL"),
                    ("SVC", "SVC"),
                    ("CSD", "CSD"),
                    ("SSP", "SSP"),
                    ("ESP", "ESP"),
                    ("MVR", "MVR"),
                    ("MKD", "MKD"),
                    ("GRD", "GRD"),
                    ("XTS", "XTS"),
                    ("RSD", "RSD"),
                    ("NPR", "NPR"),
                    ("BIF", "BIF"),
                    ("MXV", "MXV"),
                    ("CHE", "CHE"),
                    ("SZL", "SZL"),
                    ("MMK", "MMK"),
                    ("BEL", "BEL"),
                    ("NLG", "NLG"),
                    ("MGA", "MGA"),
                    ("UYU", "UYU"),
                    ("ZMW", "ZMW"),
                    ("PAB", "PAB"),
                    ("GBP", "GBP"),
                    ("CLE", "CLE"),
                    ("TMT", "TMT"),
                    ("XFO", "XFO"),
                    ("RON", "RON"),
                    ("TRL", "TRL"),
                    ("ZRN", "ZRN"),
                    ("ILP", "ILP"),
                    ("CSK", "CSK"),
                    ("PHP", "PHP"),
                    ("KPW", "KPW"),
                    ("GWE", "GWE"),
                    ("YUR", "YUR"),
                    ("GHS", "GHS"),
                    ("VUV", "VUV"),
                    ("PGK", "PGK"),
                    ("AED", "AED"),
                    ("KRO", "KRO"),
                    ("LAK", "LAK"),
                    ("COU", "COU"),
                    ("SYP", "SYP"),
                    ("XOF", "XOF"),
                    ("BND", "BND"),
                    ("ALL", "ALL"),
                    ("GEK", "GEK"),
                    ("ANG", "ANG"),
                    ("SCR", "SCR"),
                    ("MNT", "MNT"),
                    ("MDL", "MDL"),
                    ("XPD", "XPD"),
                    ("ARL", "ARL"),
                    ("SIT", "SIT"),
                    ("USD", "USD"),
                    ("RUB", "RUB"),
                    ("IQD", "IQD"),
                    ("KRW", "KRW"),
                    ("GMD", "GMD"),
                    ("ZWD", "ZWD"),
                    ("VND", "VND"),
                    ("CLF", "CLF"),
                    ("AWG", "AWG"),
                    ("XCD", "XCD"),
                    ("MVP", "MVP"),
                    ("UYW", "UYW"),
                    ("SDG", "SDG"),
                    ("BAM", "BAM"),
                    ("XRE", "XRE"),
                    ("SOS", "SOS"),
                    ("HKD", "HKD"),
                    ("PES", "PES"),
                    ("ISK", "ISK"),
                    ("LUL", "LUL"),
                    ("YUM", "YUM"),
                    ("MGF", "MGF"),
                    ("MUR", "MUR"),
                    ("BRB", "BRB"),
                    ("BSD", "BSD"),
                    ("BDT", "BDT"),
                    ("XXX", "XXX"),
                    ("FJD", "FJD"),
                    ("KZT", "KZT"),
                    ("EUR", "EUR"),
                    ("CNY", "CNY"),
                    ("INR", "INR"),
                    ("VNN", "VNN"),
                    ("JPY", "JPY"),
                    ("AOA", "AOA"),
                    ("ZAR", "ZAR"),
                    ("AZN", "AZN"),
                    ("AOR", "AOR"),
                    ("GNF", "GNF"),
                    ("KHR", "KHR"),
                    ("KRH", "KRH"),
                    ("PLZ", "PLZ"),
                    ("UAK", "UAK"),
                    ("BRL", "BRL"),
                    ("XAU", "XAU"),
                    ("ESA", "ESA"),
                    ("BBD", "BBD"),
                    ("NIC", "NIC"),
                    ("VES", "VES"),
                    ("BHD", "BHD"),
                    ("NOK", "NOK"),
                    ("CHW", "CHW"),
                    ("MKN", "MKN"),
                    ("COP", "COP"),
                    ("UAH", "UAH"),
                    ("CYP", "CYP"),
                    ("GTQ", "GTQ"),
                    ("ILR", "ILR"),
                    ("YUN", "YUN"),
                    ("XBC", "XBC"),
                    ("BRE", "BRE"),
                    ("ROL", "ROL"),
                    ("BRZ", "BRZ"),
                    ("THB", "THB"),
                    ("LUC", "LUC"),
                    ("HRD", "HRD"),
                    ("SDP", "SDP"),
                    ("NAD", "NAD"),
                    ("RHD", "RHD"),
                    ("PTE", "PTE"),
                    ("MCF", "MCF"),
                    ("NZD", "NZD"),
                    ("MRU", "MRU"),
                    ("NIO", "NIO"),
                    ("LTL", "LTL"),
                    ("BOP", "BOP"),
                    ("MAF", "MAF"),
                    ("MZE", "MZE"),
                    ("PKR", "PKR"),
                    ("NGN", "NGN"),
                    ("BYN", "BYN"),
                    ("ETB", "ETB"),
                    ("PEI", "PEI"),
                    ("DEM", "DEM"),
                    ("DJF", "DJF"),
                    ("XAF", "XAF"),
                    ("MRO", "MRO"),
                    ("LYD", "LYD"),
                    ("ALK", "ALK"),
                    ("SBD", "SBD"),
                    ("MTL", "MTL"),
                    ("LVR", "LVR"),
                    ("CRC", "CRC"),
                    ("EGP", "EGP"),
                    ("BGL", "BGL"),
                    ("JOD", "JOD"),
                    ("BEC", "BEC"),
                    ("MDC", "MDC"),
                    ("BUK", "BUK"),
                    ("BOL", "BOL"),
                    ("LVL", "LVL"),
                    ("SAR", "SAR"),
                    ("AUD", "AUD"),
                    ("CLP", "CLP"),
                    ("FKP", "FKP"),
                    ("GYD", "GYD"),
                    ("UGX", "UGX"),
                    ("ZWL", "ZWL"),
                    ("AFA", "AFA"),
                    ("CHF", "CHF"),
                    ("BMD", "BMD"),
                    ("ATS", "ATS"),
                    ("CDF", "CDF"),
                    ("MLF", "MLF"),
                    ("SEK", "SEK"),
                    ("AMD", "AMD"),
                    ("MZM", "MZM"),
                    ("SHP", "SHP"),
                    ("DDM", "DDM"),
                    ("LTT", "LTT"),
                    ("SDD", "SDD"),
                    ("BGN", "BGN"),
                    ("BRC", "BRC"),
                    ("KES", "KES"),
                    ("LBP", "LBP"),
                    ("XSU", "XSU"),
                    ("MOP", "MOP"),
                    ("AOK", "AOK"),
                    ("GWP", "GWP"),
                ],
                default="BTC",
                max_length=3,
            ),
        ),
    ]
