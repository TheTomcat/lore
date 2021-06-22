import React, { useReducer } from 'react'
import './char.css';
const ACTIONS = {

}

const reducer = (state, action) => {

}

const CharacterSheet = () => {
    const [ state, dispatch ] = useReducer(reducer, {

    });
    return (
<form className="charsheet" id="charsheet">
  <div className="header">
    <section className="charname">
      <label for="charname">Character Name</label><input name="charname" id="charname" placeholder="Character Name" />
    </section>
    <section className="misc">
      <ul>
        <li>
          <label for="classlevel">Class + Level</label><input name="classlevel" placeholder="Class 1" />
        </li>
        <li>
          <label for="background">Background</label><input name="background" placeholder="Background" />
        </li>
        <li>
          <label for="playername">Player Name</label><input name="playername" placeholder="Player Name"/>
        </li>
        <li>
          <label for="race">Race</label><input name="race" placeholder="Race" />
        </li>
        <li>
          <label for="alignment">Alignment</label><input name="alignment" placeholder="Alignment" />
        </li>
        <li>
          <label for="experiencepoints">Experience Points</label><input name="experiencepoints" placeholder="0" />
        </li>
      </ul>
    </section>
  </div>
  <div className="main">
    <section>
      <section className="attributes">
        <div className="scores">
          <ul>
            <li>
              <div className="score">
                <label for="Strengthscore">Strength</label><input name="Strengthscore" placeholder="10" className="stat"/>
              </div>
              <div className="modifier">
                <input name="Strengthmod" placeholder="+0" className="statmod"/>
              </div>
            </li>
            <li>
              <div className="score">
                <label for="Dexterityscore">Dexterity</label><input name="Dexterityscore" placeholder="10" className="stat"/>
              </div>
              <div className="modifier">
                <input name="Dexteritymod" placeholder="+0" className="statmod"/>
              </div>
            </li>
            <li>
              <div className="score">
                <label for="Constitutionscore">Constitution</label><input name="Constitutionscore" placeholder="10" className="stat"/>
              </div>
              <div className="modifier">
                <input name="Constitutionmod" placeholder="+0" className="statmod"/>
              </div>
            </li>
            <li>
              <div className="score">
                <label for="Intelligencescore">Intelligence</label><input name="Intelligencescore" placeholder="10" className="stat"/>
              </div>
              <div className="modifier">
                <input name="Intelligencemod" placeholder="+0" className="statmod"/>
              </div>
            </li>
            <li>
              <div className="score">
                <label for="Wisdomscore">Wisdom</label><input name="Wisdomscore" placeholder="10" className="stat"/>
              </div>
              <div className="modifier">
                <input name="Wisdommod" placeholder="+0" />
              </div>
            </li>
            <li>
              <div className="score">
                <label for="Charismascore">Charisma</label><input name="Charismascore" placeholder="10" className="stat"/>
              </div>
              <div className="modifier">
                <input name="Charismamod" placeholder="+0" className="statmod"/>
              </div>
            </li>
          </ul>
        </div>
        <div className="attr-applications">
          <div className="proficiencybonus box">
            <div className="label-container">
              <label for="inspiration">Inspiration</label>
            </div>
            <input name="inspiration" placeholder="" />
          </div>
          <div className="proficiencybonus box">
            <div className="label-container">
              <label for="proficiencybonus">Proficiency Bonus</label>
            </div>
            <input name="proficiencybonus" placeholder="+2" />
          </div>
          <div className="saves list-section box">
            <ul>
              <li>
                <label for="Strength-save">Strength</label><input name="Strength-save" placeholder="+0" type="text" /><input name="Strength-save-prof" type="checkbox" />
              </li>
              <li>
                <label for="Dexterity-save">Dexterity</label><input name="Dexterity-save" placeholder="+0" type="text" /><input name="Dexterity-save-prof" type="checkbox" />
              </li>
              <li>
                <label for="Constitution-save">Constitution</label><input name="Constitution-save" placeholder="+0" type="text" /><input name="Constitution-save-prof" type="checkbox" />
              </li>
              <li>
                <label for="Intelligence-save">Intelligence</label><input name="Intelligence-save" placeholder="+0" type="text" /><input name="Intelligence-save-prof" type="checkbox" />
              </li>
              <li>
                <label for="Wisdom-save">Wisdom</label><input name="Wisdom-save" placeholder="+0" type="text" /><input name="Wisdom-save-prof" type="checkbox" />
              </li>
              <li>
                <label for="Charisma-save">Charisma</label><input name="Charisma-save" placeholder="+0" type="text" /><input name="Charisma-save-prof" type="checkbox" />
              </li>
            </ul>
            <div className="label">
              Saving Throws
            </div>
          </div>
          <div className="skills list-section box">
            <ul>
              <li>
                <label for="Acrobatics">Acrobatics <span className="skill">(Dex)</span></label><input name="Acrobatics" placeholder="+0" type="text" /><input name="Acrobatics-prof" type="checkbox" />
              </li>
              <li>
                <label for="Animal Handling">Animal Handling <span className="skill">(Wis)</span></label><input name="Animal Handling" placeholder="+0" type="text" /><input name="Animal Handling-prof" type="checkbox" />
              </li>
              <li>
                <label for="Arcana">Arcana <span className="skill">(Int)</span></label><input name="Arcana" placeholder="+0" type="text" /><input name="Arcana-prof" type="checkbox" />
              </li>
              <li>
                <label for="Athletics">Athletics <span className="skill">(Str)</span></label><input name="Athletics" placeholder="+0" type="text" /><input name="Athletics-prof" type="checkbox" />
              </li>
              <li>
                <label for="Deception">Deception <span className="skill">(Cha)</span></label><input name="Deception" placeholder="+0" type="text" /><input name="Deception-prof" type="checkbox" />
              </li>
              <li>
                <label for="History">History <span className="skill">(Int)</span></label><input name="History" placeholder="+0" type="text" /><input name="History-prof" type="checkbox" />
              </li>
              <li>
                <label for="Insight">Insight <span className="skill">(Wis)</span></label><input name="Insight" placeholder="+0" type="text" /><input name="Insight-prof" type="checkbox" />
              </li>
              <li>
                <label for="Intimidation">Intimidation <span className="skill">(Cha)</span></label><input name="Intimidation" placeholder="+0" type="text" /><input name="Intimidation-prof" type="checkbox" />
              </li>
              <li>
                <label for="Investigation">Investigation <span className="skill">(Int)</span></label><input name="Investigation" placeholder="+0" type="text" /><input name="Investigation-prof" type="checkbox" />
              </li>
              <li>
                <label for="Medicine">Medicine <span className="skill">(Wis)</span></label><input name="Medicine" placeholder="+0" type="text" /><input name="Medicine-prof" type="checkbox" />
              </li>
              <li>
                <label for="Nature">Nature <span className="skill">(Int)</span></label><input name="Nature" placeholder="+0" type="text" /><input name="Nature-prof" type="checkbox" />
              </li>
              <li>
                <label for="Perception">Perception <span className="skill">(Wis)</span></label><input name="Perception" placeholder="+0" type="text" /><input name="Perception-prof" type="checkbox" />
              </li>
              <li>
                <label for="Performance">Performance <span className="skill">(Cha)</span></label><input name="Performance" placeholder="+0" type="text" /><input name="Performance-prof" type="checkbox" />
              </li>
              <li>
                <label for="Persuasion">Persuasion <span className="skill">(Cha)</span></label><input name="Persuasion" placeholder="+0" type="text" /><input name="Persuasion-prof" type="checkbox" />
              </li>
              <li>
                <label for="Religion">Religion <span className="skill">(Int)</span></label><input name="Religion" placeholder="+0" type="text" /><input name="Religion-prof" type="checkbox" />
              </li>
              <li>
                <label for="Sleight of Hand">Sleight of Hand <span className="skill">(Dex)</span></label><input name="Sleight of Hand" placeholder="+0" type="text" /><input name="Sleight of Hand-prof" type="checkbox" />
              </li>
              <li>
                <label for="Stealth">Stealth <span className="skill">(Dex)</span></label><input name="Stealth" placeholder="+0" type="text" /><input name="Stealth-prof" type="checkbox" />
              </li>
              <li>
                <label for="Survival">Survival <span className="skill">(Wis)</span></label><input name="Survival" placeholder="+0" type="text" /><input name="Survival-prof" type="checkbox" />
              </li>
            </ul>
            <div className="label">
              Skills
            </div>
          </div>
        </div>
      </section>
    </section>
    <section>
      <section className="combat">
        <div className="armorclass">
          <div>
            <label for="ac">Armor Class</label><input name="ac" placeholder="10" type="text" />
          </div>
        </div>
        <div className="initiative">
          <div>
            <label for="initiative">Initiative</label><input name="initiative" placeholder="+0" type="text" />
          </div>
        </div>
        <div className="speed">
          <div>
            <label for="speed">Speed</label><input name="speed" placeholder="30ft" type="text" />
          </div>
        </div>
        <div className="armorclass">
          <div>
            <label for="currenthp">Current Hit Points</label><input name="currenthp" placeholder="10" type="text" />
          </div>
        </div>
        <div className="armorclass">
          <div>
            <label for="maxhp">Hit Point Maximum</label><input name="maxhp" placeholder="10" type="text" />
          </div>
        </div>
        <div className="armorclass">
          <div>
            <label for="temphp">Temporary Hit Points</label><input name="temphp" placeholder="0" type="text" />
          </div>
        </div>
        <div className="hitdice">
          <div>
            <div className="total">
              <label for="totalhd">Total</label><input name="totalhd" placeholder="_d__" type="text" />
            </div>
            <div className="remaining">
              <label for="remaininghd">Hit Dice</label><input name="remaininghd" type="text" />
            </div>
          </div>
        </div>
        <div className="deathsaves">
          <div>
            <div className="label">
              <label>Death Saves</label>
            </div>
            <div className="marks">
              <div className="deathsuccesses">
                <label>Successes</label>
                <div className="bubbles">
                  <input name="deathsuccess1" type="checkbox" />
                  <input name="deathsuccess2" type="checkbox" />
                  <input name="deathsuccess3" type="checkbox" />
                </div>
              </div>
              <div className="deathfails">
                <label>Failures</label>
                <div className="bubbles">
                  <input name="deathfail1" type="checkbox" />
                  <input name="deathfail2" type="checkbox" />
                  <input name="deathfail3" type="checkbox" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <div className="otherprofs box textblock">
          <label for="otherprofs">Other Proficiencies and Languages</label><textarea name="otherprofs">=== ARMOR&#013;&#010;&#013;&#010;=== WEAPONS&#013;&#010;&#013;&#010;=== TOOLS&#013;&#010;&#013;&#010;=== LANGUAGES</textarea>
        </div>
    </section>
    <section>
      <section className="flavor">
        <div className="personality">
          <label for="defenses">Defenses & Active Conditions</label><textarea name="defenses"></textarea>
        </div>
        <div className="ideals">
          <label for="savenotes">Saving Throw Notes</label><textarea name="savenotes"></textarea>
        </div>
        <div className="bonds">
          <label for="movement">Movement Speeds</label><textarea name="movement"></textarea>
        </div>
        <div className="flaws">
          <label for="senses">Senses</label><textarea name="senses"></textarea>
        </div>
      </section>
      <div className="passive-perception box">
        <div className="label-container">
          <label for="passiveperception">Passive Wisdom (Perception)</label>
        </div>
        <input name="passiveperception" placeholder="10" />
      </div>
      <div className="passive-perception box">
        <div className="label-container">
          <label for="passiveinsight">Passive Wisdom (Insight)</label>
        </div>
        <input name="passiveinsight" placeholder="10" />
      </div>
      <div className="passive-perception box">
        <div className="label-container">
          <label for="passiveinvestigation">Passive Intelligence (Investigation)</label>
        </div>
        <input name="passiveinvestigation" placeholder="10" />
      </div>
    </section>

  </div>

  <div className="header">
      <section className="attacksandspellcasting">
          <div>
            <label>Attacks & Spellcasting</label>
            <table>
              <thead>
                <tr>
                  <th>
                    Name
                  </th>
                  <th>
                    Attack Bonus
                  </th>
                  <th>
                    Damage/Type
                  </th>
                  <th colspan="2">
                    Notes
                  </th>
                </tr>
              </thead>
              <tbody id="attacktable">
                <tr>
                  <td>
                    <input name="atkname0" type="text" />
                  </td>
                  <td>
                    <input name="atkbonus0" type="text" />
                  </td>
                  <td>
                    <input name="atkdamage0" type="text" />
                  </td>
                  <td colspan="2">
                    <input name="atknotes0" type="text" />
                  </td>
                </tr>
                <tr>
                  <td>
                    <input name="atkname1" type="text" />
                  </td>
                  <td>
                    <input name="atkbonus1" type="text" />
                  </td>
                  <td>
                    <input name="atkdamage1" type="text" />
                  </td>
                  <td colspan="2">
                    <input name="atknotes1" type="text" />
                  </td>
                </tr>
              </tbody>
            </table>
            <span>
              <button name="button-addattack" type="button" onclick="add_attack()" style={{width:"20%"}}>Add New Attack</button>
              <button name="button-removeattack" type="button" onclick="remove_last_row('attacktable')" style={{width:"20%"}}>Remove Attack</button>
            </span>
            <textarea name="attacksnotes">=== ACTIONS&#013;&#010;&#013;&#010;=== BONUS ACTIONS&#013;&#010;&#013;&#010;=== REACTIONS&#013;&#010;&#013;&#010;=== LIMITED USE</textarea>
          </div>
      </section>
  </div>

  <hr className="pageborder" />

  <div className="header">
    <section className="attacksandspellcasting" id="spellslots">
      <div>
        <label>Spell Slots</label>
        <table>
          <thead>
            <tr>
              <th>Level</th>
              <th>1</th>
              <th>2</th>
              <th>3</th>
              <th>4</th>
              <th>5</th>
              <th>6</th>
              <th>7</th>
              <th>8</th>
              <th>9</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Available</td>
              <td><input name="spellslots1" type="text" placeholder=""/></td>
              <td><input name="spellslots2" type="text" placeholder=""/></td>
              <td><input name="spellslots3" type="text" placeholder=""/></td>
              <td><input name="spellslots4" type="text" placeholder=""/></td>
              <td><input name="spellslots5" type="text" placeholder=""/></td>
              <td><input name="spellslots6" type="text" placeholder=""/></td>
              <td><input name="spellslots7" type="text" placeholder=""/></td>
              <td><input name="spellslots8" type="text" placeholder=""/></td>
              <td><input name="spellslots9" type="text" placeholder=""/></td>
            </tr>
            <tr>
              <td>Maximum</td>
              <td><input name="spellslotsmax1" type="text" placeholder="0"/></td>
              <td><input name="spellslotsmax2" type="text" placeholder="0"/></td>
              <td><input name="spellslotsmax3" type="text" placeholder="0"/></td>
              <td><input name="spellslotsmax4" type="text" placeholder="0"/></td>
              <td><input name="spellslotsmax5" type="text" placeholder="0"/></td>
              <td><input name="spellslotsmax6" type="text" placeholder="0"/></td>
              <td><input name="spellslotsmax7" type="text" placeholder="0"/></td>
              <td><input name="spellslotsmax8" type="text" placeholder="0"/></td>
              <td><input name="spellslotsmax9" type="text" placeholder="0"/></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <section className="attacksandspellcasting" id="pactslots" style={{width:"20%"}}>
        <div>
          <label>Pact Slots</label>
          <table>
            <thead>
              <tr>
                <th>Level</th>
                <th><input name="pactlevel" type="text" placeholder=""/></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Available</td>
                <td><input name="pactslots1" type="text" placeholder=""/></td>
              </tr>
              <tr>
                <td>Maximum</td>
                <td><input name="pactslotsmax1" type="text" placeholder="0"/></td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
  </div>

  <div className="header">
    <section className="attacksandspellcasting" id="spells">
      <div>
        <label>Spell List</label>
        <table>
          <thead>
            <tr>
              <th>
                Prepared
              </th>
              <th>
                Name
              </th>
              <th>
                Level
              </th>
              <th>
                Source
              </th>
              <th>
                Attack/Save
              </th>
              <th>
                Cast Time
              </th>
              <th>
                Range/Shape
              </th>
              <th>
                Duration
              </th>
              <th>
                Components
              </th>
              <th>
                Notes
              </th>
            </tr>
          </thead>
          <tbody id="spelltable">
            <tr>
              <td>
                <input name="spellprep1" type="checkbox" />
              </td>
              <td>
                <input name="spellname0" type="text" />
              </td>
              <td>
                <input name="spelllevel0" type="text" />
              </td>
              <td>
                <input name="spellsource0" type="text" />
              </td>
              <td>
                <input name="spellattacksave0" type="text" />
              </td>
              <td>
                <input name="spelltime0" type="text" />
              </td>
              <td>
                <input name="spellrange0" type="text" />
              </td>
              <td>
                <input name="spellduration0" type="text" />
              </td>
              <td>
                <input name="spellcomponents0" type="text" />
              </td>
              <td>
                <input name="spellnotes0" type="text" />
              </td>
            </tr>
            <tr>
              <td>
                <input name="spellprep1" type="checkbox" />
              </td>
              <td>
                <input name="spellname1" type="text" />
              </td>
              <td>
                <input name="spelllevel1" type="text" />
              </td>
              <td>
                <input name="spellsource1" type="text" />
              </td>
              <td>
                <input name="spellattacksave1" type="text" />
              </td>
              <td>
                <input name="spelltime1" type="text" />
              </td>
              <td>
                <input name="spellrange1" type="text" />
              </td>
              <td>
                <input name="spellduration1" type="text" />
              </td>
              <td>
                <input name="spellcomponents1" type="text" />
              </td>
              <td>
                <input name="spellnotes1" type="text" />
              </td>
            </tr>
          </tbody>
        </table>
        <span>
          <button name="button-addspell" type="button" onclick="add_spell()" style={{width:"20%"}}>Add New Spell</button>
          <button name="button-removespell" type="button" onclick="remove_last_row('spelltable')" style={{width:"20%"}}>Remove Spell</button>
        </span>
        <textarea name="spellsnotes" placeholder="Additional spell notes"></textarea>
      </div>
    </section>
  </div>

  <hr className="pageborder" />

  <div className="header">
      <section className="encumberance" id="encumberancetable" style={{width:"30%"}}>
        <div>
            <label style={{order:0,padding:"5px"}}>Encumberance</label>
            <div>
              <table>
                <tbody>
                  <tr>
                    <th>Weight Carried</th>
                  </tr>
                  <tr>
                    <td><input name="weightcarried" id="weightcarried" placeholder="0" readonly/></td>
                  </tr>
                  <tr>
                    <th>Weight Capacity</th>
                  </tr>
                  <tr>
                    <td><input name="weightcapacity" placeholder="0" /></td>
                  </tr>
                </tbody>
              </table>
              <textarea name="encumberancenotes" placeholder="Additional encumberance notes" style={{height:"12em"}}></textarea>
            </div>
        </div>
      </section>

      <section className="currency" style={{width:"30%"}}>
        <div>
          <label style={{order:0,padding:"5px"}}>Currency</label>
          <div className="money">
            <ul>
              <li>
                <label for="pp">pp</label><input name="pp" />
              </li>
              <li>
                <label for="gp">gp</label><input name="gp" />
              </li>
              <li>
                <label for="ep">ep</label><input name="ep" />
              </li>
              <li>
                <label for="sp">sp</label><input name="sp" />
              </li>
              <li>
                <label for="cp">cp</label><input name="cp" />
              </li>
            </ul>
          </div>
        </div>
      </section>

      <section className="attacksandspellcasting" id="attunement">
        <div>
          <label style={{order:0,padding:"5px"}}>Attunement</label>
          <table>
            <thead>
              <tr>
                <th>Attuned Magic Items</th>
              </tr>
            </thead>
            <tbody id="attunementtable">
              <tr><td><input name="attunement0" type="text" /></td></tr>
              <tr><td><input name="attunement1" type="text" /></td></tr>
              <tr><td><input name="attunement2" type="text" /></td></tr>
            </tbody>
          </table>
          <span>
            <button name="button-addattunement" type="button" onclick="add_attunement()" style={{width:"45%"}}>Add Attunement Slot</button>
            <button name="button-removeattunement" type="button" onclick="remove_last_row('attunementtable')" style={{width:"45%"}}>Remove Attunement Slot</button>
          </span>
          <textarea name="attunementsnotes" placeholder="Additional attunement notes"></textarea>
        </div>
      </section>
  </div>

  <div className="header">
      <section className="attacksandspellcasting" id="inventory">
          <div>
            <label>Inventory</label>
            <table>
              <thead>
                <tr>
                  <th>
                    Equipped
                  </th>
                  <th>
                    Name
                  </th>
                  <th>
                    Count
                  </th>
                  <th>
                    Weight
                  </th>
                  <th>
                    Value
                  </th>
                  <th>
                    Notes
                  </th>
                </tr>
              </thead>
              <tbody id="inventorytable">
                <tr>
                  <td>
                    <input name="itemequipped0" type="checkbox" />
                  </td>
                  <td>
                    <input name="itemname0" type="text" />
                  </td>
                  <td>
                    <input name="itemcount0" type="text" onchange="calc_carry_weight()" />
                  </td>
                  <td>
                    <input name="itemweight0" type="text" onchange="calc_carry_weight()" />
                  </td>
                  <td>
                    <input name="itemvalue0" type="text" />
                  </td>
                  <td>
                    <input name="itemnotes0" type="text" />
                  </td>
                </tr>
                <tr>
                  <td>
                    <input name="itemequipped1" type="checkbox" />
                  </td>
                  <td>
                    <input name="itemname1" type="text" />
                  </td>
                  <td>
                    <input name="itemcount1" type="text" onchange="calc_carry_weight()" />
                  </td>
                  <td>
                    <input name="itemweight1" type="text" onchange="calc_carry_weight()" />
                  </td>
                  <td>
                    <input name="itemvalue1" type="text" />
                  </td>
                  <td>
                    <input name="itemnotes1" type="text" />
                  </td>
                </tr>
              </tbody>
            </table>
            <span>
              <button name="button-additem" type="button" onclick="add_inventory()" style={{width:'20%'}}>Add New Item</button>
              <button name="button-removeitem" type="button" onclick="remove_last_row('inventorytable');calc_carry_weight();" style={{width:"20%"}}>Remove Item</button>
            </span>
            <textarea name="inventorynotes" placeholder="Additional inventory notes"></textarea>
          </div>
      </section>
  </div>

  <hr className="pageborder" />

  <div className="main">
      <section className="features" id="feautres-left">
        <div>
          <label for="features-l">Features, Traits, + Feats</label><textarea name="features-l"></textarea>
        </div>
      </section>
      <section className="features" id="feautres-center">
        <div>
          <label for="features-c">Features, Traits, + Feats</label><textarea name="features-c"></textarea>
        </div>
      </section>
      <section className="features" id="feautres-right">
        <div>
          <label for="features-r">Features, Traits, + Feats</label><textarea name="features-r"></textarea>
        </div>
      </section>
  </div>

  <hr className="pageborder" />

  <div className="header">
    <section className="misc" id="misc-desc">
      <ul>
        <li>
          <label for="gender">Gender</label><input name="gender" placeholder="Gender" />
        </li>
        <li>
          <label for="age">Age</label><input name="age" placeholder="Age" />
        </li>
        <li>
          <label for="height">Height</label><input name="height" placeholder="Height" />
        </li>
        <li>
          <label for="weight">Weight</label><input name="weight" placeholder="Weight" />
        </li>
        <li>
          <label for="faith">Faith</label><input name="faith" placeholder="Faith" />
        </li>
        <li>
          <label for="skin">Skin</label><input name="skin" placeholder="Skin" />
        </li>
        <li>
          <label for="eyes">Eyes</label><input name="eyes" placeholder="Eyes" />
        </li>
        <li>
          <label for="hair">Hair</label><input name="hair" placeholder="Hair" />
        </li>
      </ul>
    </section>
  </div>
  <div className="main">
      <section className="features" id="allies-orgs-enemies">
        <div>
          <label for="organizations">Allies, Organizations, + Enemies</label><textarea name="organizations">=== ALLIES&#013;&#010;&#013;&#010;=== ORGANIZATIONS&#013;&#010;&#013;&#010;=== ENEMIES</textarea>
        </div>
      </section>
      <section className="features" id="backstory">
        <div>
          <label for="backstory">Character Backstory</label><textarea name="backstory"></textarea>
        </div>
      </section>
      <section>
          <section className="flavor">
              <div className="personality">
                <label for="personality">Personality</label><textarea name="personality"></textarea>
              </div>
              <div className="ideals">
                <label for="ideals">Ideals</label><textarea name="ideals"></textarea>
              </div>
              <div className="bonds">
                <label for="bonds">Bonds</label><textarea name="bonds"></textarea>
              </div>
              <div className="flaws">
                <label for="flaws">Flaws</label><textarea name="flaws"></textarea>
              </div>
            </section>
      </section>
  </div>

  <hr className="pageborder" />

  <div className="main">
      <section className="features" id="notes-left">
        <div>
          <label for="notes-l">Additional Notes</label><textarea name="notes-l"></textarea>
        </div>
      </section>
      <section className="features" id="notes-center">
        <div>
          <label for="notes-c">Additional Notes</label><textarea name="notes-c"></textarea>
        </div>
      </section>
      <section className="features" id="notes-right">
        <div>
          <label for="notes-r">Additional Notes</label><textarea name="notes-r"></textarea>
        </div>
      </section>
  </div>
  <div className="main">
    <input name="rows_attacks" type="hidden" value="2"/>
    <input name="rows_attunements" type="hidden" value="3"/>
    <input name="rows_inventory" type="hidden" value="2"/>
    <input name="rows_spells" type="hidden" value="2"/>
  </div> 
</form>
    )
}
export default CharacterSheet;