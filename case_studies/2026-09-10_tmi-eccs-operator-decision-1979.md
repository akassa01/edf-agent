---
case_id: tmi-eccs-operator-decision-1979
title: "The Procedure in the Room: Three Mile Island and the Problem of Protocol Authority"
case_type: documented
mode: retrospective
scale: individual
region: "Americas (Middletown, Pennsylvania, USA)"
recency: historical
year: 1979
archetype_dominant: engineer
crowded_out_mode: "thinking"
flag: "expert training in high-stakes technical systems creates procedural authority that, at its extreme, becomes cognitively inaccessible to the person it governs — the redesign that helps is institutional, not individual"
rubric_version: 1
---

# The Procedure in the Room: Three Mile Island and the Problem of Protocol Authority

At 4:01 AM on March 28, 1979, the pilot-operated relief valve on Unit 2's pressuriser opened. This was designed behaviour. The reactor had just scrammed — automatically shut itself down — following a turbine failure, and the PORV was releasing excess pressure exactly as it was supposed to. At 4:11 AM, the valve was commanded to close. The control panel indicator light confirmed that the close command had been sent. In the control room at the Three Mile Island nuclear generating station near Middletown, Pennsylvania, the operators saw what they needed to see.

The valve had not closed. Its bellows assembly had failed. Coolant was escaping from the primary system at approximately 220 gallons per minute. But the indicator light showed "closed command received," not "valve physically closed" — a distinction that was known to the reactor's designers at Babcock & Wilcox and not flagged to operators as significant. The operators were not flying blind: they had instruments. They read those instruments through a framework that told them what kind of accident they were in. And that framework was wrong.

What followed across the next sixteen hours is the cleanest available demonstration of what the Emergency Operating Procedures in nuclear plants were doing and what they could not do. The operators at TMI-2 were doing their jobs. They were following the Emergency Operating Procedures for a high-pressure transient — the class of accident the symptom profile most closely resembled, given what their instruments showed. When the Emergency Core Cooling System activated automatically, it appeared, within that framework, to be overinjecting water into a system that was already at high pressure. At approximately 4:38 AM, the senior operator reduced ECCS flow. This was the rational action within the high-pressure transient procedure. It was exactly the wrong action for a loss-of-coolant accident, which is what was actually happening.

The Engineer's instinct is procedural, and in nuclear operations the procedure is the safety system. The Emergency Operating Procedures at TMI were event-based: diagnose what type of accident you are in, follow the corresponding procedure. This architecture had a specific virtue — speed and reliability in well-characterised scenarios — and a specific failure mode: it provided no mechanism for questioning whether the event categorisation was correct. The operators could not step outside the procedure to ask "what kind of accident am I actually in?" They could only execute the procedure for the accident they had diagnosed. The procedure was the answer and the question simultaneously.

The Scientist sees the problem clearly from outside the control room. NRC engineers examining the symptom profile retrospectively — dropping primary pressure despite the PORV indicator showing closed, rising core temperatures, contradictory pressuriser level readings as steam voids formed in the uncovered fuel — identified the PORV as the probable source within hours. The operators, inside the room with the same data, took sixteen hours. The difference was not competence. The operators were among the best-trained personnel in the industry. The difference was what the Scientist can do from outside — trace the physical implications of each reading back to first principles about what must be happening to the coolant inventory — and what the operator inside the procedure could not do, because the procedure was doing the reasoning for them.

The Humanist counts the consequences in a different register. A million people in the Harrisburg, Lancaster, and York region were hearing contradictory messages from official sources about whether to evacuate. NRC Commissioner Hendrie told the Governor's office, "I would get out." Governor Thornburgh told residents that only pregnant women and children within five miles needed to consider leaving. Neither was lying; each was communicating a different slice of an uncertainty that the official communication system had not been designed to convey. The five days of the crisis produced in its surrounding communities something the reactor's instruments did not show: a durable loss of trust in the institutions responsible for managing technical risk. The machinery had a near-miss. The relationship between technical expertise and public confidence did not recover.

Where was X? Not the moment the PORV stuck open, which was a mechanical failure outside the operators' control. The moment was 4:38 AM, in the control room, when the senior operator reduced ECCS flow. This was the fulcrum. A single diagnostic check in the EOP — "before any ECCS throttling, verify that core subcooling margin is positive" — would have stopped the action. The operators would have looked at the subcooling calculation, found it negative, and been forced to consider that their event diagnosis was wrong. The diagnostic check was conceptually simple. It was absent from the procedure because the procedure had been designed, licensed, and validated without it. Eighteen months before the accident, a Babcock & Wilcox internal memo had documented exactly this class of confusion from a prior incident at another plant — ECCS flow reduced prematurely by operators who believed they were in a high-pressure transient. The memo was distributed internally. It did not result in an EOP revision.

The question 1+1 revealed is: who was asking what? The operators were answering "what does the high-pressure EOP require?" The reactor was answering "what is the current state of my coolant inventory?" These were different questions. The EOP manual addressed only the first. There was no shared framework for the second — no symptom-based diagnostic layer that could interrupt the procedural response and ask the physical question. 1+1 produced two separate ones: a procedural response to a diagnosed accident category, and an actual loss-of-coolant accident, proceeding simultaneously and diverging at 4:38 AM.

The binary presented was follow the EOP (which the operators did) or deviate from the EOP without authorisation (which would have been grounds for disciplinary action under the training culture of 1979). The 18th camel was not a choice between these two: it was a structural change in how the EOP was designed. A symptom-based layer — mandatory before any major coolant system action — would have required operators to verify that the current physical symptom profile was consistent with their event categorisation before proceeding. This was not a new idea. It was the exact reform the NRC mandated in the aftermath of the accident, implemented across the industry within two years. The solution existed before the accident. It required the accident to be implemented.

What a principled pragmatist at the institutional level — at B&W, at the NRC — could have done after the 1977/78 memo was not complicated: issue an emergency operational bulletin requiring operators at all B&W-design reactors to verify PORV physical status by monitoring the discharge line temperature during any pressure transient. This workaround required no new instrumentation. At TMI-2, the PORV discharge line temperature was measurable; it was approximately 280°F when it should have been ambient. Operators who checked would have known within thirty minutes that coolant was escaping. The bulletin was not issued. The memo was filed.

The same analysis that makes this episode valuable as a teaching case makes it disturbing as a governance case: the operators did what they were supposed to do, with the training they were supposed to have, using the procedures that had been licensed as correct. The failure was institutional before it was operational. Expertise had been encoded in a document that made the reflective questioning of that document — which is what the physical state of the reactor required — institutionally unavailable at the moment it was most needed.

This is what the Solomon Paradox looks like in a control room. The wisdom the operators needed — step back and reason about what must be physically true — was available to them as trained nuclear engineers thinking about someone else's reactor. They could not apply it to their own. Proximity does not just limit perspective. In high-stakes technical systems with tight procedures and high urgency, proximity eliminates the reflective stance that perspective requires.

*(The flag this episode raises is one that institutional redesign cannot fully resolve. Expert training in high-stakes technical systems creates procedural authority that, at its extreme, becomes cognitively inaccessible to the person it governs. The operator at the decisive moment cannot simply decide to set aside the procedure and reason from first principles — the procedure is the reasoning, the way expertise has been internalised and encoded. Principled pragmatism can prescribe self-distancing and framework-questioning; it cannot make that prescription available to the person whose expertise consists precisely in having internalised the framework so deeply that questioning it no longer presents itself as an option. The institutional redesign — mandatory symptom-based layers, incident-to-procedure feedback pathways — is the correct response. It cannot guarantee that the next class of accident, which the symptom-based procedure has also not anticipated, will be survived the same way.)*

---

**Problem** — A nuclear operator must respond in real time to an accident whose physical character does not match the event category his procedure assumes, using instruments and procedures that provide no mechanism for questioning the event categorisation.

**Stakeholders** — The Unit 2 operators (principal decision-makers; trained correctly for the procedure they used); Babcock & Wilcox (reactor designer; held the 1977/78 memo); the NRC (licensing authority; had accepted event-based EOPs); 900,000 residents in the surrounding communities (principal harm-bearers of the public communication failure); the global nuclear industry (whose expansion trajectory ended at TMI).

**Binding constraint** — The Emergency Operating Procedures, validated and licensed as correct, contained no mechanism for questioning whether the event categorisation was correct — making the one reflective step that would have changed the outcome institutionally unavailable under the conditions that required it.

**Decision pathway** — Redesign: revise the EOPs to embed a symptom-based diagnostic layer before any major coolant system action, requiring operators to verify physical consistency before executing the procedure for a diagnosed event category.

**Tools** — (1) Symptom-based EOP diagnostic layer: before any ECCS throttling, verify core subcooling margin is positive and current symptoms are consistent with the assumed event category — changing the operator's interaction from execution to verification. (2) Mandatory operational anomaly review protocol: any field report identifying anomalous ECCS or PORV behaviour triggers automatic EOP review — institutionalising the feedback path the 1977/78 memo did not follow. (3) Independent physical diagnostic card at each operator station: five observable symptoms that indicate loss-of-coolant regardless of event diagnosis — providing a second-order, physically-grounded decision layer outside the EOP framework.

**Metrics** — (1) Time from symptom onset to PORV-as-source diagnosis in subsequent B&W reactor incidents. (2) Percentage of operational anomaly reports resulting in EOP review within 30 days. (3) Operator accuracy in identifying loss-of-coolant scenarios in mixed-symptom simulator evaluations — testing whether the redesigned procedure changes actual behaviour under realistic conditions.

**90-day commitment** — Week 1: B&W issues emergency bulletin requiring PORV discharge line temperature verification during all pressure transients (no new instrumentation required; identifies stuck PORV within 30 minutes). Week 4: joint NRC-B&W-utility working group convened on symptom-based EOP supplement. Day 90: draft supplement complete and in NRC technical review; simulator testing begun.

---

**References**

President's Commission on the Accident at Three Mile Island (1979). *The Report of the President's Commission on the Accident at Three Mile Island* (Kemeny Report). Washington, D.C.: U.S. Government Printing Office.

Nuclear Regulatory Commission (1980). *Three Mile Island: A Report to the Commissioners and to the Public* (Rogovin Report). Washington, D.C.: NRC.

Walker, J. Samuel (2004). *Three Mile Island: A Nuclear Crisis in Historical Perspective*. Berkeley: University of California Press.

Perrow, Charles (1984). *Normal Accidents: Living with High-Risk Technologies*. New York: Basic Books.

Mahaffey, James (2014). *Atomic Accidents: A History of Nuclear Meltdowns and Disasters*. New York: Pegasus Books.
