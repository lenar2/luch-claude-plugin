import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class TestClaudeAutonomy(unittest.TestCase):
 def test_full_mcp_endpoint_untouched(self):
  c=json.loads((ROOT/'.mcp.json').read_text())
  self.assertEqual(c['mcpServers']['luch']['url'],'https://luch.lenarsalimov.ru/luch/core/mcp')
 def test_twelve_guidance_skills_not_twelve_tools(self):
  skills=list((ROOT/'skills').glob('*/SKILL.md'))
  self.assertEqual(len(skills),12)
  for p in skills:
   t=p.read_text()
   self.assertIn('**LUCH task-level autonomy:**',t,p)
   self.assertNotIn('**Public Core 0.1.5 availability gate:**',t,p)
   self.assertNotIn('Ask for confirmation before',t,p)
   self.assertNotIn('Ask confirmation for',t,p)
 def test_current_snapshot_consistent(self):
  snap=json.loads((ROOT/'tools/luch_connected_snapshot.json').read_text())
  self.assertEqual(snap['total'],166)
  names=[t['name'] for t in snap['tools']]
  self.assertEqual(len(names),len(set(names)))
  self.assertTrue(all(0<len(n)<=64 for n in names))
  groups={k:sum(t['group']==k for t in snap['tools']) for k in snap['groups']}
  self.assertEqual(groups,snap['groups'])
  self.assertEqual([groups['local_browser'],groups['server_browser'],groups['github'],groups['server'],groups['other']],[41,20,23,10,72])
 def test_triage_labels_not_fake_annotations(self):
  snap=json.loads((ROOT/'tools/luch_connected_snapshot.json').read_text())
  for t in snap['tools']:
   self.assertIn(t['reviewClass'],('mutation_or_interaction','read_candidate','manual_review'))
   self.assertNotIn('annotations',t)
 def test_browser_and_computer_workflows_complete_actions(self):
  for item in ('luch-browser','luch-local-browser','luch-computer','luch-workflows'):
   t=(ROOT/'skills'/item/'SKILL.md').read_text()
   self.assertIn('click',t.lower())
   self.assertIn('host',t.lower())
if __name__=='__main__':unittest.main()
