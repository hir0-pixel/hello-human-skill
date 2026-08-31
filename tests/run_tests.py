#!/usr/bin/env python3
"""Run Hello Human detector validation on bundled samples."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from score import score, PASS_THRESHOLD

SAMPLES = {
    "EMAIL_AI": {
        "text": 'Dear Sarah, I hope this email finds you well. Additionally, it is important to note that our team has been working diligently to streamline the onboarding process and foster a more robust ecosystem for collaboration. Furthermore, we would like to leverage these comprehensive improvements to enhance your experience.',
        "expect_pass": False,
    },
    "EMAIL_HUMAN": {
        "text": "Hi Sarah, Quick follow-up from Tuesday. We tightened the onboarding checklist and cut two redundant approval steps. Should save your team about a day on the first hire. One gap: we still don't have your SSO vendor listed. Can you send that name by Thursday?",
        "expect_pass": True,
    },
    "BLOG_AI": {
        "text": "In today's fast-paced digital landscape, remote work has become a pivotal moment in the evolving landscape of modern employment. Organizations must delve into comprehensive strategies to streamline operations. Furthermore, it is important to note that leaders should prioritize employee wellbeing. In conclusion, remote work represents a testament to the enduring resilience of the modern workforce.",
        "expect_pass": False,
    },
    "BLOG_HUMAN": {
        "text": "Remote work didn't kill offices. It killed the idea that everyone needs the same schedule. Some teams I talk to are genuinely faster async. Others just have longer Slack threads. If you're a manager still debating remote vs office, you're asking the wrong question. We cut our weekly standup from 45 minutes to 15 once we stopped making everyone listen to updates that belonged in a doc.",
        "expect_pass": True,
    },
    "ESSAY_AI": {
        "text": "Additionally, it is important to note that relocating to a new city represents a pivotal moment in one's personal journey. This transformation not only reshapes daily routines but also fosters a deeper connection to community and belonging. Furthermore, many individuals find that embracing change serves as a testament to their resilience in an ever-evolving landscape. In conclusion, the decision to move is a comprehensive step toward personal growth and meaningful experiences.",
        "expect_pass": False,
    },
    "ESSAY_HUMAN": {
        "text": "I moved to Portland in 2019 because rent in Oakland finally beat my salary. That sounds dramatic. It wasn't — I just got tired of sending half my paycheck to a landlord who wouldn't fix a leaking bathroom for eleven months.\n\nThe city surprised me. I expected rain jokes and coffee snobs. Instead I got neighbors who actually loan tools and a bus line that runs late but at least runs. I still miss my friends in the Bay. We text less than we promised we would. That's on me as much as distance.\n\nLast winter I tried to grow tomatoes on a balcony that gets maybe four hours of sun. Total harvest: three cherry tomatoes and a lot of aphids. My roommate ate two of the tomatoes before I could photograph them for Instagram, which is probably the right ending for that story.\n\nPeople ask if I'll move back. Maybe when my parents need help, or maybe never. Portland isn't perfect — the homeless crisis is visible in a way that makes you feel useless walking past — but it's home enough that I know which grocery store has the good bulk oats.\n\nI work remotely now, which I swore I'd never enjoy. Turns out I like cooking lunch at home and not fighting for parking at 8:55 a.m. My manager still schedules meetings that could've been an email. Some things don't change with geography.\n\nIf you're thinking about leaving an expensive city, don't treat it like a movie montage. Budget for lonely Tuesdays. Also budget for when your car check-engine light comes on and you don't know a mechanic yet. I learned that the hard way in February.",
        "expect_pass": True,
    },
    "LINKEDIN_AI": {
        "text": "I'm thrilled to share that our team has successfully leveraged cutting-edge strategies to streamline our billing infrastructure! This journey has been a testament to cross-functional collaboration and robust engineering practices. Furthermore, it is important to note that we delved into comprehensive solutions that enhance scalability. Grateful for this pivotal moment. Let's continue to foster innovation together! #Leadership #Growth",
        "expect_pass": False,
    },
    "LINKEDIN_HUMAN": {
        "text": 'We shipped the billing refactor on a Friday. I still think that was stupid.\n\nThree engineers, six weeks, and one production incident that lasted 22 minutes because we missed a timezone edge case in legacy invoices. Not our proudest moment. The fix was boring: add tests, roll back, patch, redeploy. The interesting part was what we learned about how little anyone on the sales team understood about proration.\n\nI spent Tuesday in a room with account managers drawing boxes on a whiteboard. No slides. Just "when does the customer actually get charged?" asked ten different ways until the room went quiet.\n\nIf you\'re leading a backend migration, budget time for translation — not code translation, people translation. Your API can be elegant and your org can still break customers because nobody owns the story between systems.\n\nWe also underestimated how many reports finance ran off the old schema. I got a Slack message at 6 p.m. from someone I\'d never met asking why ARR looked "weird." It wasn\'t weird. The definition changed. We hadn\'t written that down anywhere public.\n\nNext time we\'re doing a cutover mid-week, with a dry run that includes sales, not just engineering. Obvious in hindsight. Hindsight always is.\n\nHappy to chat if you\'re mid-migration and drowning in edge cases. DMs open.',
        "expect_pass": True,
    },
    "MARKETING_AI": {
        "text": 'Introducing a revolutionary desk lamp designed to transform your workspace into a sanctuary of productivity. Our comprehensive solution leverages innovative LED technology to foster focus and wellbeing. Additionally, it is important to note that this robust product serves as a testament to modern design. Experience the difference today and embark on a journey toward a more vibrant work environment.',
        "expect_pass": False,
    },
    "MARKETING_HUMAN": {
        "text": 'Our desk lamp isn\'t for everyone.\n\nIf you want something that blends into beige furniture and whispers "corporate wellness," skip us. The Kova lamp is loud on purpose: matte black arm, one physical dial, no app, no firmware updates at 2 a.m.\n\nWe built it because my cofounder got migraines from cheap LEDs that flicker at frequencies your eyes feel before your brain names it. We sourced a driver that costs more than some entire lamps on Amazon. Margin suffers. Sleep doesn\'t.\n\nShips in two days from Ohio. Returns are simple — send it back, we recycle the aluminum. Warranty is three years because anything shorter would embarrass us.\n\n$89. Not on sale. Not "limited time." Same price since March.\n\nWe don\'t do influencer bundles or fake MSRP strikethroughs. The box is plain cardboard because fancy packaging ends up in the trash anyway.\n\nIf you need RGB pulsing for your stream setup, we\'re the wrong brand. If you want to read at night without feeling like you\'re under stadium lights, we\'re probably fine.\n\nQuestions go to support@kovalamp.example — a human reads it, usually within a day. Might be me. I still pack orders when we\'re slammed.',
        "expect_pass": True,
    },
    "CASUAL_TEXT_AI": {
        "text": 'Hey! I hope this message finds you well. Additionally, I wanted to reach out regarding our upcoming gathering on Saturday. It is important to note that we are excited to foster a wonderful time together. Furthermore, please let me know if you need anything else. Looking forward to connecting!',
        "expect_pass": False,
    },
    "CASUAL_TEXT_HUMAN": {
        "text": "yo are you still coming saturday\n\nmom called me twice about the potato salad situation and I told her you're handling it but idk if that was a lie\n\nalso Jake's bringing that speaker that sounds like trash so maybe warn people\n\nI can grab ice on the way if you text me before noon. otherwise we're drinking warm soda like animals\n\nseriously though let me know about the salad thing. mom will 100% bring three tubs of coleslaw if she thinks we're unprepared\n\noh and park on the street not in the driveway. dad's still mad about the oil stain from mark's truck lol\n\nif you're running late just text. not calling the group chat again like last time when everyone panicked for no reason\n\nsee you whenever. bring cups if you remember. we always forget cups",
        "expect_pass": True,
    },
    "GROK_STYLE_AI": {
        "text": "Dating apps didn't ruin romance — they merely underscore the empirical reality that human connection correlates with intentionality rather than algorithmic optimization. The causal chain is clear: swipe culture fosters performative vulnerability while authentic intimacy remains elusive. One must delve into the tapestry of modern courtship to grasp this pivotal transformation.",
        "expect_pass": False,
    },
    "GROK_STYLE_HUMAN": {
        "text": 'Everyone online has a take on whether dating apps "ruined" romance. Most of those takes are lazy.\n\nI deleted Hinge for six months in 2024. Not as a personality trait — I just got bored of the same opening messages and the performative hiking photos. Met someone at a friend\'s birthday instead. We lasted four months. Fine. Not a TED talk.\n\nThe app didn\'t fail me. I was showing up tired and treating matches like customer support tickets. Swipe, small talk, ghost. Repeat. Hard to call that romance in any medium.\n\nWould I go back? Probably. I\'m lazy on weeknights. But I\'m done pretending the algorithm owes me a soulmate. It\'s a bulletin board with better UX. Act accordingly.\n\nMy friends argue about "intentionality" like it\'s a vitamin. Maybe. I just think people want shortcuts when they\'re lonely and then get mad when shortcuts feel cheap. Fair.\n\nI don\'t have a grand theory. I have a drawer full of charger cables and a history of liking people who are bad at texting back. Apps didn\'t invent that problem.',
        "expect_pass": True,
    },
    "ACADEMIC_AI": {
        "text": 'Furthermore, it is important to note that urban heat mitigation strategies serve as a comprehensive framework for enhancing community resilience. This study delves into the evolving landscape of tree canopy interventions and underscores the pivotal role of green infrastructure. Additionally, our findings foster a more robust understanding of thermal comfort in metropolitan environments.',
        "expect_pass": False,
    },
    "ACADEMIC_HUMAN": {
        "text": "Prior work on urban heat islands often treats tree canopy as a uniform intervention, which obscures block-level variation in impervious surface cover. In our 2023 pilot along Southeast Powell Boulevard, we paired LiDAR-derived shade maps with pedestrian-reported discomfort scores collected via a simple SMS prompt (n = 412 over six weeks).\n\nWe found shade alone did not predict reported comfort once afternoon bus frequency was included in the model. Riders waiting 25 minutes or longer reported heat stress scores 1.4 points higher on a 7-point scale, independent of canopy percentage. That interaction was not significant in our smaller 2021 dataset, which suggests sample timing matters as much as planting schedules.\n\nWe hesitate to generalize beyond Portland's street grid. Still, municipal planting programs that ignore transit wait times may be optimizing the wrong variable. Future work should link shade investment to stop amenities — benches, real-time arrival data — not just crown diameter targets.\n\nOne limitation: our SMS sample skewed toward smartphone users comfortable texting city numbers. We probably underheard older riders and recent immigrants who still rely on paper schedules at the stop.\n\nReplication materials and anonymized response logs are archived with OSU's data repository. Happy to share R scripts; they're messy but commented.",
        "expect_pass": True,
    },
}

def main():
    failed = 0
    print(f"Hello Human detector validation (threshold <= {PASS_THRESHOLD})\n")
    for name, sample in SAMPLES.items():
        result = score(sample["text"])
        ok = result["pass"] == sample["expect_pass"]
        mark = "OK" if ok else "MISMATCH"
        if not ok:
            failed += 1
        print(
            f"[{mark}] {name}: prob={result['ai_probability']:.3f} "
            f"pass={result['pass']} (expected {sample['expect_pass']})"
        )
    print()
    if failed:
        print(f"{failed} sample(s) mismatched expectations.")
        sys.exit(1)
    print("All samples scored as expected.")
    sys.exit(0)


if __name__ == "__main__":
    main()
